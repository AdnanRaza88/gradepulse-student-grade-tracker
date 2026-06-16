# GradePulse - Student Grade Tracker

Professional student grade management system with FastAPI backend and Streamlit frontend. Includes AI-powered study coach using Groq and LangChain.

## Features
- Add, view, update and delete student grades
- Automatic percentage and grade calculation
- AI Study Coach for personalized tips and routines
- Clean, modern neumorphic interface
- Bulk operations ready

## Setup

1. Clone the repository
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your GROQ_API_KEY
4. Start backend: `uvicorn backend.main:app --reload`
5. Start frontend: `streamlit run frontend/app.py`

## Project Structure
- `backend/` → FastAPI application
- `frontend/` → Streamlit user interface
