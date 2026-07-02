import streamlit as st
import pandas as pd

from utils import load_risk_data
from styles import load_css

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="Risk Analysis",
    page_icon="⚠️",
    layout="wide"
)

load_css()

risk_df = load_risk_data()

# ---------------------------------------
# Sidebar
# ---------------------------------------
st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.markdown("---")

# ---------------------------------------
# Header
# ---------------------------------------
st.title("⚠️ Property Risk Analysis")

st.markdown("""
Analyze the investment risk of a property using the business rules
developed during the project.
""")

st.markdown("---")
st.subheader("🏠 Select Property")

col1, col2 = st.columns(2)

with col1:
    city = st.selectbox(
        "City",
        sorted(risk_df["City"].unique())
    )

with col2:
    location = st.selectbox(
        "Location",
        sorted(
            risk_df[
                risk_df["City"] == city
            ]["Location"].unique()
        )
    )

analyze_btn = st.button(
    "⚠️ Analyze Risk",
    type="primary",
    use_container_width=True
)
if analyze_btn:

    filtered = risk_df[
        (risk_df["City"] == city) &
        (risk_df["Location"] == location)
    ]

    if filtered.empty:
        st.error("No matching property found.")
        st.stop()

    property_data = filtered.iloc[0]

    risk_score = property_data["Risk_Score"]
    risk_category = property_data["Risk_Category"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Risk Score",
            f"{risk_score:.1f}/100"
        )

    with col2:
        st.metric(
            "Risk Category",
            risk_category
        )

    st.caption(f"📍 {city} • {location}")

    if risk_category == "Low Risk":
        st.success("🟢 Low Risk Property")
    elif risk_category == "Medium Risk":
        st.warning("🟡 Medium Risk Property")
    else:
        st.error("🔴 High Risk Property")