import streamlit as st
from utils import load_model_comparison
import pandas as pd
from styles import load_css

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Real Estate Price Prediction System",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Global Styles
load_css()

st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.caption("Smart Property Analytics")
st.sidebar.markdown("---")

# -----------------------------
# Title
# -----------------------------
st.image("assets/banner.png", use_container_width=True)

st.title("🏠 AI-Powered Real Estate Price Prediction System")
st.markdown("### Intelligent Property Analytics & Investment Dashboard")
st.markdown("---")

# -----------------------------
# Project Description
# -----------------------------
feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    st.success("💰 Property Price Prediction")
    st.success("📈 Investment Recommendation")
    st.success("⚠️ Risk Analysis")
    st.success("📅 Future Price Forecast")

with feature_col2:
    st.success("🧠 Explainable AI")
    st.success("📊 Exploratory Data Analysis")
    st.success("🆚 Property Comparison")
    st.success("📌 Market Insights")

st.markdown("---")

# -----------------------------
# Project Statistics
# -----------------------------
stats_df = pd.read_csv("models/future_price_forecast.csv")
comparison_df = load_model_comparison()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Properties", f"{len(stats_df):,}")

with col2:
    st.metric("Cities", stats_df["City"].nunique())

with col3:
    st.metric("Features", len(stats_df.columns))

with col4:
    st.metric("ML Models", len(comparison_df))

st.markdown("---")

# -----------------------------
# Model Comparison
# -----------------------------
st.subheader("📊 Model Performance Comparison")

st.dataframe(
    comparison_df,
    use_container_width=True
)

best_model = comparison_df.sort_values(
    by="R² Score",
    ascending=False
).iloc[0]

st.success(
    f"🏆 Best Model: {best_model['Model']} | "
    f"R² Score: {best_model['R² Score']:.4f}"
)

st.subheader("🔄 AI Workflow")

st.markdown(
    "Dataset → EDA → Feature Engineering → Machine Learning → Price Prediction → Investment Recommendation → Risk Analysis → Future Forecast → Explainable AI"
)

st.markdown("---")

# -----------------------------
# Navigation
# -----------------------------
st.subheader("📂 Dashboard Modules")

st.info("""
Use the left sidebar to navigate through the dashboard.

Available modules:

• 📊 EDA Dashboard

• 💰 Property Price Prediction

• 📈 Investment Recommendation

• ⚠️ Risk Analysis

• 📅 Future Price Forecast

• 🧠 Explainable AI

• 📑 Property Comparison

• 📌 Market Insights
""")

st.markdown("---")

st.markdown("---")
st.markdown(
    """
<div class='footer'>
<b>Developed by Het Patel</b><br>
AI/ML Internship Project • Real Estate Intelligence Platform<br>
Powered by Python • Streamlit • Scikit-Learn • SHAP
</div>
""",
    unsafe_allow_html=True,
)