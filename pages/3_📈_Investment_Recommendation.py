import streamlit as st
import pandas as pd
import numpy as np

from utils import load_model, load_recommendation_data, format_price
from styles import load_css

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Investment Recommendation",
    page_icon="📈",
    layout="wide"
)

load_css()

model = load_model()
recommendation_df = load_recommendation_data()

st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.markdown("---")

st.title("📈 Investment Recommendation Engine")

st.markdown("""
Evaluate whether a property is a **BUY**, **HOLD**, or **SELL**
using the trained AI model and business rules.
""")

st.markdown("---")

# ==========================================================
# Property Details
# ==========================================================

st.subheader("🏠 Property Details")

col1, col2 = st.columns(2)

with col1:
    city = st.selectbox(
        "Select City",
        sorted(recommendation_df["City"].unique()),
        key="inv_city"
    )

    listed_price = st.number_input(
        "Listed Price (₹)",
        min_value=100000,
        value=5000000,
        step=100000,
        key="listed_price"
    )

    area = st.number_input(
        "Area (sq.ft.)",
        min_value=100,
        max_value=10000,
        value=1200,
        step=50,
        key="inv_area"
    )

with col2:
    city_locations = sorted(
        recommendation_df[
            recommendation_df["City"] == city
        ]["Location"].unique()
    )

    location = st.selectbox(
        "Select Location",
        city_locations,
        key="inv_location"
    )

    bhk = st.selectbox(
        "BHK",
        [1, 2, 3, 4, 5],
        key="inv_bhk"
    )

    resale = st.selectbox(
        "Resale Property",
        ["No", "Yes"],
        key="inv_resale"
    )

st.markdown("---")

analyze_btn = st.button(
    "📈 Analyze Investment",
    type="primary",
    use_container_width=True
)

# ==========================================================
# Investment Analysis
# ==========================================================
if analyze_btn:

    input_data = {
        "City": city,
        "Location": location,
        "Area": area,
        "BHK": bhk,
        "Resale": 1 if resale == "Yes" else 0,
    }

    # Initialize remaining features expected by the model
    for feature in model.feature_names_in_:
        if feature not in input_data:
            input_data[feature] = 0

    input_df = pd.DataFrame([input_data])

    predicted_price = np.expm1(model.predict(input_df)[0])

    difference = predicted_price - listed_price
    difference_percent = (difference / listed_price) * 100

    if difference_percent >= 10:
        recommendation = "🟢 BUY"
        reason = "The property appears undervalued compared to the AI estimated market value."
    elif difference_percent >= -5:
        recommendation = "🟡 HOLD"
        reason = "The listed price is close to the AI estimated market value."
    else:
        recommendation = "🔴 SELL"
        reason = "The listed price appears higher than the AI estimated market value."

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Listed Price", format_price(listed_price))

    with c2:
        st.metric("AI Predicted Price", format_price(predicted_price))

    with c3:
        st.metric("Difference", f"{difference_percent:.2f}%")

    st.markdown("### 📈 Investment Recommendation")
    st.success(recommendation)
    st.info(reason)