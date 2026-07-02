import streamlit as st

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis")

st.markdown("""
This page presents the exploratory data analysis performed on the real estate dataset.
""")

st.markdown("---")

st.subheader("Price Distribution")

st.image(
    "images/price_distribution.png",
    use_container_width=True
)

st.markdown("---")

st.subheader("Correlation Heatmap")

st.image(
    "images/correlation_heatmap.png",
    use_container_width=True
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Price by City")
    st.image(
        "images/price_by_city.png",
        use_container_width=True
    )

with col2:
    st.subheader("Price by BHK")
    st.image(
        "images/price_by_bhk.png",
        use_container_width=True
    )

st.markdown("---")

st.subheader("Area vs Price")

st.image(
    "images/area_vs_price.png",
    use_container_width=True
)