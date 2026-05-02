import streamlit as st
import pandas as pd

def show_state_view(state_df, city_df):
    st.header("State-Level Dashboard")

    # Step 1: Get selected state from session
    selected_state = st.session_state.get("selected_state")

    if not selected_state:
        st.warning("Please select a state from the India overview.")
        return

    # Step 2: Filter state-level data
    df_state = state_df[state_df["State / Union Territory"] == selected_state]

    if df_state.empty:
        st.error("No data available for the selected state.")
        return

    row = df_state.iloc[0]

    # Step 3: Display State Metrics
    st.subheader(f"📍 {selected_state}")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Price per Sqft (₹)",
        f"₹{row['Price/sqft (₹)']:,}"
    )

    col2.metric(
        "Median Price 2025 (₹ Lakh)",
        f"{row['Median House Price (₹ Lakh) -2025']:.2f}"
    )

    col3.metric(
        "YoY Growth (%)",
        f"{row['YoY Price Growth (%)']*100:.2f}%"
    )

    st.write("**Region:**", row["Region"])
    st.write("**Market Tier:**", row["Market Tier"])

    # Step 4: City Selection
    available_cities = sorted(
        city_df[city_df["City"].notna()]["City"].unique()
    )

    selected_city = st.selectbox(
        "Select a City",
        available_cities
    )

    st.session_state.selected_city = selected_city
  
