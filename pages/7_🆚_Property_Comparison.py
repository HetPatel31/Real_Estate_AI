

import streamlit as st
import pandas as pd

from styles import load_css

st.set_page_config(
    page_title="Property Comparison",
    page_icon="🆚",
    layout="wide"
)

load_css()

st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.markdown("---")

st.title("🆚 Property Comparison Dashboard")
st.markdown("Compare two properties using AI predictions, forecasts and investment recommendations.")
st.markdown("---")

# Load Dataset
df = pd.read_csv("models/future_price_forecast.csv")

st.subheader("Select Properties")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏠 Property A")
    city_a = st.selectbox("City", sorted(df["City"].unique()), key="city_a")
    location_a = st.selectbox(
        "Location",
        sorted(df[df["City"] == city_a]["Location"].unique()),
        key="location_a"
    )
    property_a = df[(df["City"] == city_a) & (df["Location"] == location_a)].iloc[0]

with col2:
    st.markdown("### 🏠 Property B")
    city_b = st.selectbox("City", sorted(df["City"].unique()), key="city_b")
    location_b = st.selectbox(
        "Location",
        sorted(df[df["City"] == city_b]["Location"].unique()),
        key="location_b"
    )
    property_b = df[(df["City"] == city_b) & (df["Location"] == location_b)].iloc[0]

st.markdown("---")

comparison = pd.DataFrame({
    "Metric": [
        "Current Price",
        "Predicted Price",
        "Recommendation",
        "1 Year Forecast",
        "3 Year Forecast",
        "5 Year Forecast"
    ],
    "Property A": [
        f"₹{property_a['Price']:,.0f}",
        f"₹{property_a['Predicted_Price']:,.0f}",
        property_a['Recommendation'],
        f"₹{property_a['Price_1_Year']:,.0f}",
        f"₹{property_a['Price_3_Years']:,.0f}",
        f"₹{property_a['Price_5_Years']:,.0f}"
    ],
    "Property B": [
        f"₹{property_b['Price']:,.0f}",
        f"₹{property_b['Predicted_Price']:,.0f}",
        property_b['Recommendation'],
        f"₹{property_b['Price_1_Year']:,.0f}",
        f"₹{property_b['Price_3_Years']:,.0f}",
        f"₹{property_b['Price_5_Years']:,.0f}"
    ]
})

st.subheader("📊 Comparison")
st.dataframe(comparison, use_container_width=True, hide_index=True)

st.markdown("---")

growth_a = ((property_a['Price_5_Years'] - property_a['Price']) / property_a['Price']) * 100
growth_b = ((property_b['Price_5_Years'] - property_b['Price']) / property_b['Price']) * 100

st.subheader("🏆 Better Investment")

if growth_a > growth_b:
    st.success(f"Property A is expected to perform better over 5 years.\n\nExpected Growth: {growth_a:.2f}%")
elif growth_b > growth_a:
    st.success(f"Property B is expected to perform better over 5 years.\n\nExpected Growth: {growth_b:.2f}%")
else:
    st.info("Both properties have similar long-term growth potential.")