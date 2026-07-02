import streamlit as st
import pandas as pd
import numpy as np

from utils import (
    load_model,
    load_recommendation_data,
    format_price
)

from styles import load_css


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Property Price Prediction",
    page_icon="💰",
    layout="wide"
)

load_css()

# -----------------------------
# Load Resources
# -----------------------------
model = load_model()
recommendation_df = load_recommendation_data()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.markdown("---")

# -----------------------------
# Header
# -----------------------------
st.title("💰 Property Price Prediction")

st.markdown(
    """
Predict the market value of a property using the trained AI model.
"""
)

st.markdown("---")
# ==========================================================
# Property Details
# ==========================================================

st.subheader("🏠 Property Details")

col1, col2 = st.columns(2)

with col1:

    city = st.selectbox(
        "Select City",
        sorted(recommendation_df["City"].unique())
    )

    area = st.number_input(
        "Area (sq.ft.)",
        min_value=100,
        max_value=10000,
        value=1200,
        step=50
    )

    resale = st.selectbox(
        "Resale Property",
        ["No", "Yes"]
    )

with col2:

    city_locations = sorted(
        recommendation_df[
            recommendation_df["City"] == city
        ]["Location"].unique()
    )

    location = st.selectbox(
        "Select Location",
        city_locations
    )

    bhk = st.selectbox(
        "BHK",
        sorted(recommendation_df["BHK"].unique())
    )

st.markdown("---")

# ==========================================================
# Amenities
# ==========================================================
st.subheader("🏢 Amenities")

amenity_features = [
    "Gymnasium", "SwimmingPool", "ClubHouse", "24X7Security",
    "PowerBackup", "CarParking", "LiftAvailable",
    "Children'splayarea", "SportsFacility", "IndoorGames",
    "ShoppingMall", "Hospital", "School"
]

amenities = {}

with st.expander("Select Available Amenities"):
    cols = st.columns(2)
    for i, feature in enumerate(amenity_features):
        with cols[i % 2]:
            amenities[feature] = st.checkbox(feature)

# ==========================================================
# Furnishing
# ==========================================================
st.subheader("🛋 Furnishing")

furnishing_features = [
    "AC", "BED", "Sofa", "Wardrobe",
    "Refrigerator", "TV", "WashingMachine",
    "Wifi", "Gasconnection"
]

furnishing = {}

with st.expander("Select Furnishing Items"):
    cols = st.columns(2)
    for i, feature in enumerate(furnishing_features):
        with cols[i % 2]:
            furnishing[feature] = st.checkbox(feature)

st.markdown("---")

predict_btn = st.button(
    "🔵 Predict Property Price",
    type="primary",
    use_container_width=True
)

# ==========================================================
# Prediction
# ==========================================================
if predict_btn:

    input_data = {
        "City": city,
        "Location": location,
        "Area": area,
        "BHK": bhk,
        "Resale": 1 if resale == "Yes" else 0,
    }

    # Get all features expected by the pipeline
    feature_names = model.feature_names_in_

    # Initialize missing features
    for feature in feature_names:
        if feature not in input_data:
            input_data[feature] = 0

    # Fill amenities
    for feature, value in amenities.items():
        input_data[feature] = int(value)

    # Fill furnishing
    for feature, value in furnishing.items():
        input_data[feature] = int(value)

    input_df = pd.DataFrame([input_data])

    predicted_log_price = model.predict(input_df)[0]
    predicted_price = np.expm1(predicted_log_price)

    st.markdown("---")
    st.subheader("💰 Estimated Property Price")
    st.success(format_price(predicted_price))