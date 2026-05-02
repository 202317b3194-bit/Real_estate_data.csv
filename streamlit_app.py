import streamlit as st
import pandas as pd

def show_city_summary_view(df):
    st.header("City-Level Dashboard")

    # ✅ Step 1: Read selected city
    if "selected_city" not in st.session_state:
        st.warning("Please select a city first.")
        return

    selected_city = st.session_state["selected_city"]

    # ✅ Step 2: Filter data for city
    city_df = df[df["City"] == selected_city]

    if city_df.empty:
        st.error("No data found for this city.")
        return

    st.subheader(f"📍 City: {selected_city}")

    # ✅ Step 3: City-level metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average Price / Sqft (₹)",
        f"₹{int(city_df['Price per Sqft (INR)S'].mean()):,}"
    )

    col2.metric(
        "Average Property Price (₹)",
        f"₹{int(city_df['Estimated Sale Price (INR)'].mean()):,}"
    )

    col3.metric(
        "Average Rental Yield (%)",
        f"{city_df['Rental Yield (%)'].mean():.2f}%"
    )

    # ✅ Step 4: Extra insights
    st.write("**Property Types Available:**")
    st.write(list(city_df["Property Type"].unique()))

    st.write("**Average Buyer Attraction Score:**",
             round(city_df["Buyer Attraction Score (1-10)"].mean(), 2))

    st.divider()

    # ✅ Step 5: Locality selection (handoff to Person 3)
    locality = st.selectbox(
        "Select Locality for Detailed View",
        sorted(city_df["Locality"].unique())
    )

    st.session_state["selected_locality"] = locality
