

import streamlit as st
import pandas as pd
import plotly.express as px

from styles import load_css

st.set_page_config(
    page_title="Future Price Forecast",
    page_icon="📈",
    layout="wide"
)

load_css()

st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.markdown("---")

st.title("📈 Future Price Forecast")
st.markdown("Forecast future property values using the AI-generated projections.")
st.markdown("---")

# Load forecast dataset
forecast_df = pd.read_csv("models/future_price_forecast.csv")

city = st.selectbox(
    "Select City",
    sorted(forecast_df["City"].unique())
)

city_df = forecast_df[forecast_df["City"] == city]

location = st.selectbox(
    "Select Location",
    sorted(city_df["Location"].unique())
)

property_data = city_df[city_df["Location"] == location].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.metric("Current Price", f"₹{property_data['Price']:,.0f}")

with col2:
    st.metric("AI Predicted Price", f"₹{property_data['Predicted_Price']:,.0f}")

st.markdown("### 📅 Future Forecast")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("1 Year", f"₹{property_data['Price_1_Year']:,.0f}")

with c2:
    st.metric("3 Years", f"₹{property_data['Price_3_Years']:,.0f}")

with c3:
    st.metric("5 Years", f"₹{property_data['Price_5_Years']:,.0f}")

chart_df = pd.DataFrame({
    "Year": ["Current", "1 Year", "3 Years", "5 Years"],
    "Price": [
        property_data["Price"],
        property_data["Price_1_Year"],
        property_data["Price_3_Years"],
        property_data["Price_5_Years"],
    ]
})

fig = px.line(
    chart_df,
    x="Year",
    y="Price",
    markers=True,
    title="Future Property Price Forecast"
)

st.plotly_chart(fig, use_container_width=True)

growth = ((property_data["Price_5_Years"] - property_data["Price"]) / property_data["Price"]) * 100

st.markdown("### 📌 Investment Summary")

if growth > 35:
    st.success(f"Excellent long-term investment.\n\nExpected 5-Year Growth: {growth:.1f}%")
elif growth > 20:
    st.info(f"Good investment opportunity.\n\nExpected 5-Year Growth: {growth:.1f}%")
else:
    st.warning(f"Moderate growth expected.\n\nExpected 5-Year Growth: {growth:.1f}%")