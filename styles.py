import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* ----------------------------------------------------
       Global App
    ---------------------------------------------------- */
    .stApp {
        background-color: #F8FAFC !important;
        color: #1E293B !important;
    }

    /* Hide Streamlit Header & Footer */
    #MainMenu,
    header,
    footer {
        visibility: hidden;
    }

    /* ----------------------------------------------------
       Sidebar
    ---------------------------------------------------- */
    section[data-testid="stSidebar"]{
        background-color:#FFFFFF !important;
        border-right:1px solid #E5E7EB;
    }

    /* Force ALL sidebar text to be dark */
    section[data-testid="stSidebar"] *{
        color:#1E293B !important;
    }

    section[data-testid="stSidebar"] label{
        color:#1E293B !important;
    }

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div{
        color:#1E293B !important;
    }

    /* Sidebar Logo */
    section[data-testid="stSidebar"] img{
        border-radius:12px;
    }

    /* ----------------------------------------------------
       Buttons
    ---------------------------------------------------- */
    .stButton > button{
        width:100%;
        border-radius:12px;
        border:none;
        background:#2563EB;
        color:white;
        font-weight:600;
        padding:0.6rem 1rem;
        transition:0.3s;
    }

    .stButton > button:hover{
        background:#1D4ED8;
        transform:translateY(-2px);
        box-shadow:0 8px 20px rgba(37,99,235,.25);
    }

    /* ----------------------------------------------------
       Metrics
    ---------------------------------------------------- */
    div[data-testid="stMetric"]{
        background:white;
        border-radius:14px;
        padding:18px;
        border:1px solid #E5E7EB;
        box-shadow:0 5px 15px rgba(0,0,0,.05);
    }

    /* ----------------------------------------------------
       DataFrames
    ---------------------------------------------------- */
    div[data-testid="stDataFrame"]{
        border-radius:12px;
        overflow:hidden;
        border:1px solid #E5E7EB;
    }

    /* ----------------------------------------------------
       Images
    ---------------------------------------------------- */
    img{
        border-radius:12px;
    }

    /* ----------------------------------------------------
       Horizontal Line
    ---------------------------------------------------- */
    hr{
        border:none;
        border-top:1px solid #E5E7EB;
        margin:1rem 0;
    }

    /* ----------------------------------------------------
       Footer
    ---------------------------------------------------- */
    .footer{
        text-align:center;
        color:#6B7280;
        padding:20px;
        font-size:14px;
    }

    </style>
    """, unsafe_allow_html=True)
