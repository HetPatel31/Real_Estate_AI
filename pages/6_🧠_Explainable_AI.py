

import streamlit as st
from PIL import Image

from styles import load_css

st.set_page_config(
    page_title="Explainable AI",
    page_icon="🧠",
    layout="wide"
)

load_css()

st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.markdown("---")

st.title("🧠 Explainable AI Dashboard")

st.markdown(
    "Understand how the AI model makes property price predictions using SHAP (SHapley Additive exPlanations)."
)

st.markdown("---")

# Load SHAP images
summary = Image.open("images/shap_summary.png")
importance = Image.open("images/shap_feature_importance.png")
waterfall = Image.open("images/shap_waterfall.png")

# SHAP Summary
st.subheader("📊 SHAP Summary Plot")
st.image(summary, use_container_width=True)
st.info(
    "The SHAP Summary Plot shows the overall impact of each feature on property price predictions. Higher SHAP values indicate a stronger influence on the model's output."
)

st.markdown("---")

# Feature Importance
st.subheader("⭐ Feature Importance")
st.image(importance, use_container_width=True)
st.info(
    "This chart ranks the most influential features used by the Random Forest model. Features appearing at the top contribute the most to prediction accuracy."
)

st.markdown("---")

# Local Explanation
st.subheader("🏠 Local Explanation")
st.image(waterfall, use_container_width=True)
st.info(
    "The Waterfall Plot explains how different property features contribute to the predicted price for an individual property. Positive values increase the predicted price, while negative values decrease it."
)