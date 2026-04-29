import streamlit as st
import pandas as pd

# =========================
# 🏠 APP CONFIG
# =========================
st.set_page_config(page_title="Chennai Real Estate Analyzer", layout="wide")

st.title("🏠 Chennai Real Estate Data Analyzer")
st.write("Upload and analyze property dataset with encoding")

# =========================
# 📂 LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("data/Chennai_RealEstate.csv")
    df = df.dropna(how="all")
    return df

df = load_data()

st.success("Dataset Loaded Successfully ✅")
st.write("Total Rows:", df.shape[0])

# Show raw data
with st.expander("📄 View Raw Data"):
    st.dataframe(df)

# =========================
# 🔄 ENCODING
# =========================
df["Parking_Code"] = df["Parking Facility Yes/No"].map({"Yes": 1, "No": 0})

df["Furnishing_Code"] = df["Furnishing Status"].map({
    "Unfurnished": 0,
    "Semi-Furnished": 1,
    "Fully Furnished": 2
})

df["Property_Type_Code"] = df["Property Type"].map({
    "Apartment": 0,
    "Villa": 1,
    "Independent House": 2
})

df["Facing_Code"] = df["Facing"].map({
    "North": 0,
    "East": 1,
    "South": 2,
    "West": 3
})

# =========================
# 📊 ENCODING RESULT
# =========================
st.subheader("🔢 Encoded Dataset Preview")

st.dataframe(df[[
    "Property Type", "Property_Type_Code",
    "Furnishing Status", "Furnishing_Code",
    "Parking Facility Yes/No", "Parking_Code",
    "Facing", "Facing_Code"
]].head(10))

# =========================
# 🔍 FILTER DATA
# =========================
st.subheader("🔍 Filter Data")

property_type = st.selectbox(
    "Select Property Type",
    df["Property Type"].unique()
)

filtered_df = df[df["Property Type"] == property_type]



st.write(f"Showing results for: {property_type}")
st.dataframe(filtered_df)
