

import streamlit as st
import pandas as pd
import plotly.express as px

from styles import load_css

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Market Insights",
    page_icon="📊",
    layout="wide"
)

load_css()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.markdown("---")

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("📊 Market Insights Dashboard")
st.markdown("AI-powered business intelligence generated from the real estate dataset.")
st.markdown("---")

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
df = pd.read_csv("models/future_price_forecast.csv")

# --------------------------------------------------
# Feature Engineering
# --------------------------------------------------
df["Growth_Percentage"] = ((df["Price_5_Years"] - df["Price"]) / df["Price"]) * 100

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
total_properties = len(df)
total_cities = df["City"].nunique()
avg_price = df["Price"].mean()
avg_growth = df["Growth_Percentage"].mean()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🏠 Total Properties", f"{total_properties:,}")

with c2:
    st.metric("🏙 Cities", total_cities)

with c3:
    st.metric("💰 Avg Price", f"₹{avg_price:,.0f}")

with c4:
    st.metric("📈 Avg 5-Year Growth", f"{avg_growth:.1f}%")

st.markdown("---")

# --------------------------------------------------
# Top Investment Locations
# --------------------------------------------------
st.subheader("🏆 Top 10 Investment Locations")

top_growth = (
    df.sort_values("Growth_Percentage", ascending=False)
      [["City", "Location", "Growth_Percentage", "Recommendation"]]
      .head(10)
)

st.dataframe(top_growth, use_container_width=True, hide_index=True)

st.markdown("---")

# --------------------------------------------------
# Recommendation Distribution
# --------------------------------------------------
st.subheader("📈 Recommendation Distribution")

recommendation_counts = df["Recommendation"].value_counts().reset_index()
recommendation_counts.columns = ["Recommendation", "Count"]

fig = px.pie(
    recommendation_counts,
    names="Recommendation",
    values="Count",
    hole=0.45,
    title="BUY / HOLD / SELL Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --------------------------------------------------
# Highest Average Price by City
# --------------------------------------------------
st.subheader("🏙 Highest Average Price by City")

city_price = (
    df.groupby("City")["Price"]
      .mean()
      .sort_values(ascending=False)
      .reset_index()
)

fig = px.bar(
    city_price,
    x="City",
    y="Price",
    title="Average Property Price by City"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --------------------------------------------------
# Market Summary
# --------------------------------------------------
st.subheader("📌 AI Market Summary")

highest_growth = top_growth.iloc[0]
highest_city = city_price.iloc[0]
buy_pct = ((df["Recommendation"] == "BUY").mean()) * 100

st.success(f"""
### 📈 Key Insights

✅ Total Properties Analysed: **{total_properties:,}**

✅ Average 5-Year Growth: **{avg_growth:.2f}%**

✅ Highest Growth Location:
**{highest_growth['Location']} ({highest_growth['City']})**

✅ Most Expensive City:
**{highest_city['City']}**

✅ BUY Recommendations:
**{buy_pct:.1f}%** of properties

✅ Most properties are expected to appreciate over the next five years.
""")