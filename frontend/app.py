import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="GradePulse", layout="wide")

# Custom Neumorphic CSS
st.markdown("""
<style>
    .stApp {
        background: #f0f0f0;
    }
    .card {
        background: #f0f0f0;
        border-radius: 20px;
        box-shadow: 8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff;
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.image("logo.jpg", width=150)

st.title("GradePulse - Student Grade Tracker")

# Sidebar Hamburger Menu (Streamlit native)
with st.sidebar:
    st.header("Menu")
    page = st.radio("Go to", ["Dashboard", "Add Grade", "All Grades", "AI Coach", "Bulk Upload"])

if page == "Add Grade":
    # Form code here...
    pass

# Add other pages similarly with clean neumorphic cards