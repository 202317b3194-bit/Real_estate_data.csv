import streamlit as st
import pandas as pd

st.set_page_config(page_title="Real Estate Analytics", layout="wide")

# ------------------- DATA LOADING -------------------
@st.cache_data
def load_data():
    return pd.read_excel("Book3.xlsx")

df = load_data()

# ------------------- UTILITY -------------------
def clean_currency(col):
    return (
        col.astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

df["Price per Sqft"] = clean_currency(df["Price per Sqft (INR)S"])
df["Sale Price"] = clean_currency(df["Estimated Sale Price (INR)"])

# ------------------- PERSON 1 -------------------
def city_selector(df):
    st.header("Person 1 – City Selection")

    city = st.selectbox(
        "Select City",
        sorted(df["City"].unique())
    )

    st.session_state["selected_city"] = city

# ------------------- PERSON 2 -------------------
def city_dashboard(df):
    st.header("Person 2 – City Level Dashboard")

    if "selected_city" not in st.session_state:
        st.warning("Please select a city first.")
        return

    city = st.session_state["selected_city"]
    city_df = df[df["City"] == city]

    st.subheader(f"📍 {city}")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Avg Price / Sqft (₹)",
        f"₹{int(city_df['Price per Sqft'].mean()):,}"
    )

    col2.metric(
        "Avg Sale Price (₹)",
        f"₹{int(city_df['Sale Price'].mean()):,}"
    )

    col3.metric(
        "Avg Rental Yield (%)",
        f"{city_df['Rental Yield (%)'].mean():.2f}%"
    )

    st.divider()

    st.write("### Property Type Distribution")
    st.bar_chart(city_df["Property Type"].value_counts())

    st.write(
        "**Avg Buyer Attraction Score:**",
        round(city_df["Buyer Attraction Score (1-10)"].mean(), 2)
    )

    st.divider()

    locality = st.selectbox(
        "Select Locality",
        sorted(city_df["Locality"].unique())
    )

    st.session_state["selected_locality"] = locality

# ------------------- PERSON 3 -------------------
def locality_dashboard(df):
    st.header("Person 3 – Locality Deep Dive")

    if "selected_city" not in st.session_state or "selected_locality" not in st.session_state:
        st.warning("Please select city & locality first.")
        return

    city = st.session_state["selected_city"]
    locality = st.session_state["selected_locality"]

    loc_df = df[
        (df["City"] == city) &
        (df["Locality"] == locality)
    ]

    st.subheader(f"📍 {locality}, {city}")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Avg Price / Sqft (₹)",
        f"₹{int(loc_df['Price per Sqft'].mean()):,}"
    )

    col2.metric(
        "Avg Sale Price (₹)",
        f"₹{int(loc_df['Sale Price'].mean()):,}"
    )

    col3.metric(
        "Avg Rental Yield (%)",
        f"{loc_df['Rental Yield (%)'].mean():.2f}%"
    )

    st.divider()

    st.write("### Property Details")
    st.dataframe(
        loc_df[[
            "Property Type",
            "Built-up Area (sqft)",
            "Bedrooms (BHK)",
            "Bathrooms",
            "Price per Sqft",
            "Sale Price",
            "Rental Yield (%)"
        ]]
    )

# ------------------- APP FLOW -------------------
st.title("🏘 Real Estate Market Intelligence System")

city_selector(df)
city_dashboard(df)
locality_dashboard(df)
