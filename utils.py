import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Common Sidebar
# -----------------------------
def setup_sidebar():
    st.sidebar.image("assets/logo.png", width=90)
    st.sidebar.title("AI Real Estate")
    st.sidebar.caption("Smart Property Analytics")
    st.sidebar.markdown("---")

# -----------------------------
# Common Page Header
# -----------------------------
def page_header(title: str, description: str):
    st.title(title)
    st.markdown(description)
    st.markdown("---")


# -----------------------------
# Load ML Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("models/best_real_estate_model.pkl")


# -----------------------------
# Load Feature Names
# -----------------------------
@st.cache_data
def load_feature_names():
    return joblib.load("models/feature_names.pkl")


# -----------------------------
# Load Model Comparison
# -----------------------------
@st.cache_data
def load_model_comparison():
    return pd.read_csv("models/model_comparison.csv")


# -----------------------------
# Load Investment Dataset
# -----------------------------
@st.cache_data
def load_investment_data():
    return pd.read_csv("models/investment_recommendation.csv")


# -----------------------------
# Load Risk Dataset
# -----------------------------
@st.cache_data
def load_risk_data():
    return pd.read_csv("models/risk_analysis.csv")


# -----------------------------
# Load Future Forecast Dataset
# -----------------------------
@st.cache_data
def load_forecast_data():
    return pd.read_csv("models/future_price_forecast.csv")


# -----------------------------
# Load Recommendation Dataset
# -----------------------------
@st.cache_data
def load_recommendation_data():
    return pd.read_csv("models/recommendation_dataset.csv")


# -----------------------------
# Price Formatter
# -----------------------------
def format_price(price):
    if pd.isna(price):
        return "N/A"
    return f"₹ {float(price):,.0f}"