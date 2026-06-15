# GradePulse - Student Grade Tracker

FastAPI backend + Streamlit UI with AI Study Coach (Groq + LangChain).

## Setup
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add GROQ_API_KEY
3. Backend: `uvicorn backend.main:app --reload`
4. Frontend: `streamlit run frontend/app.py`