import streamlit as st
from styles import load_css

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Global CSS
load_css()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.image("assets/logo.png", width=90)
st.sidebar.title("AI Real Estate")
st.sidebar.caption("Smart Property Analytics")
st.sidebar.markdown("---")

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("📊 Exploratory Data Analysis")

st.markdown("""
This page presents the exploratory data analysis performed on the real estate dataset.
""")

st.markdown("---")

# --------------------------------------------------
# Price Distribution
# --------------------------------------------------
st.subheader("💰 Price Distribution")

st.image(
    "images/price_distribution.png",
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Correlation Heatmap
# --------------------------------------------------
st.subheader("🔥 Correlation Heatmap")

st.image(
    "images/correlation_heatmap.png",
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Price by City & BHK
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏙️ Price by City")
    st.image(
        "images/price_by_city.png",
        use_container_width=True
    )

with col2:
    st.subheader("🏠 Price by BHK")
    st.image(
        "images/price_by_bhk.png",
        use_container_width=True
    )

st.markdown("---")

# --------------------------------------------------
# Area vs Price
# --------------------------------------------------
st.subheader("📈 Area vs Price")

st.image(
    "images/area_vs_price.png",
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Top Locations
# --------------------------------------------------
st.subheader("📍 Top Property Locations")

st.image(
    "images/top_locations.png",
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# Footer
# --------------------------------------------------
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
