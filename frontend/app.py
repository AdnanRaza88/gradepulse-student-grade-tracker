import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000/api")

st.set_page_config(page_title="GradePulse", layout="wide")

# Clean Neumorphic Light Theme
st.markdown("""
<style>
    .stApp {
        background: #f8f9fc;
    }
    .card {
        background: #f0f3f8;
        border-radius: 16px;
        box-shadow: 6px 6px 12px #d1d5db, -6px -6px 12px #ffffff;
        padding: 24px;
        margin: 12px 0;
    }
    .stButton>button {
        background: #3b82f6;
        color: white;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.image("logo.jpg", width=180)

st.title("GradePulse")
st.markdown("Student Grade Tracker")

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select", ["Dashboard", "Add Grade", "All Grades", "AI Coach"])

if page == "Add Grade":
    st.subheader("Add New Grade")
    with st.form("add_grade_form"):
        student_name = st.text_input("Student Name", placeholder="Enter full name")
        subject = st.text_input("Subject")
        col1, col2 = st.columns(2)
        with col1:
            marks_obtained = st.number_input("Marks Obtained", min_value=0.0, step=0.1)
        with col2:
            total_marks = st.number_input("Total Marks", min_value=1.0, value=100.0, step=0.1)
        semester = st.text_input("Semester")
        notes = st.text_area("Notes", height=100)
        
        submitted = st.form_submit_button("Save Grade")
        if submitted:
            if not student_name or not subject or not semester:
                st.error("Please fill all required fields")
            else:
                data = {
                    "student_name": student_name.strip(),
                    "subject": subject.strip(),
                    "marks_obtained": marks_obtained,
                    "total_marks": total_marks,
                    "semester": semester.strip(),
                    "notes": notes.strip() if notes else None
                }
                try:
                    response = requests.post(f"{BACKEND_URL}/grades/", json=data)
                    if response.status_code == 200:
                        st.success("Grade saved successfully")
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error("Could not connect to backend")

elif page == "All Grades":
    st.subheader("All Grades")
    try:
        response = requests.get(f"{BACKEND_URL}/grades/")
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No grades recorded yet")
        else:
            st.error("Failed to load grades")
    except:
        st.error("Backend not reachable")

elif page == "AI Coach":
    st.subheader("Study Coach")
    grade_id = st.number_input("Grade ID", min_value=1, step=1)
    if st.button("Get Advice"):
        try:
            response = requests.post(f"{BACKEND_URL}/grades/{grade_id}/study-tips")
            if response.status_code == 200:
                result = response.json()
                st.markdown("### Study Tips")
                st.write(result["tips"])
                st.markdown("### Daily Study Routine")
                st.write(result["routine"])
            else:
                st.error("Grade not found")
        except:
            st.error("Could not connect to AI coach")

else:  # Dashboard
    st.subheader("Overview")
    st.write("Use the sidebar to manage grades and access AI coaching.")

st.caption("GradePulse - Clean Student Performance Tracker")
