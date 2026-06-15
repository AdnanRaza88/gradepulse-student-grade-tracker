from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import create_db_and_tables
from backend.routers.grades import router as grades_router

app = FastAPI(title="GradePulse API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(grades_router, prefix="/api")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "GradePulse API is running"}