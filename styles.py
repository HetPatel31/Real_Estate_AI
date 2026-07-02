import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* App Background */
    .stApp {
        background: #F5F7FB;
        color: #1F2937;
    }

    /* Hide Streamlit chrome */
    #MainMenu, header, footer {
        visibility: hidden;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1rem;
        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(37,99,235,0.18);
    }

    /* Inputs */
    .stSelectbox, .stNumberInput, .stTextInput {
        border-radius: 10px;
    }

    /* Metric Cards */
    .metric-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 20px;
        border-left: 5px solid #2563EB;
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        transition: all 0.25s ease;
        margin-bottom: 15px;
    }

    .metric-card:hover {
        transform: translateY(-4px);
    }

    .metric-value {
        font-size: 32px;
        font-weight: 700;
        color: #2563EB;
    }

    .metric-title {
        font-size: 15px;
        color: #6B7280;
    }

    /* Generic Cards */
    .custom-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        border: 1px solid #EEF2F7;
        margin: 16px 0;
    }

    /* Section Titles */
    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 10px;
    }

    /* Horizontal Rule */
    hr {
        border: none;
        border-top: 1px solid #E5E7EB;
        margin: 1.2rem 0;
    }

    /* Images */
    img {
        border-radius: 12px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6B7280;
        padding: 20px;
        font-size: 14px;
    }

    </style>
    """, unsafe_allow_html=True)