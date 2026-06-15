from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from backend.models import Grade
from backend.schemas import GradeCreate, GradeResponse, BulkUploadResponse
from backend.database import get_session
from backend.ai.groq_client import get_study_tips, get_daily_routine
import pandas as pd
from typing import List

router = APIRouter()

@router.post("/grades/", response_model=GradeResponse)
def create_grade(grade: GradeCreate, session: Session = Depends(get_session)):
    db_grade = Grade(**grade.model_dump())
    db_grade.percentage = (db_grade.marks_obtained / db_grade.total_marks) * 100
    if db_grade.percentage >= 90:
        db_grade.grade = "A"
    elif db_grade.percentage >= 75:
        db_grade.grade = "B"
    elif db_grade.percentage >= 60:
        db_grade.grade = "C"
    else:
        db_grade.grade = "Fail"
    session.add(db_grade)
    session.commit()
    session.refresh(db_grade)
    return db_grade

@router.get("/grades/", response_model=List[GradeResponse])
def get_all_grades(session: Session = Depends(get_session)):
    return session.exec(select(Grade)).all()

@router.get("/grades/{id}", response_model=GradeResponse)
def get_grade(id: int, session: Session = Depends(get_session)):
    grade = session.get(Grade, id)
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    return grade

@router.put("/grades/{id}", response_model=GradeResponse)
def update_grade(id: int, grade: GradeCreate, session: Session = Depends(get_session)):
    db_grade = session.get(Grade, id)
    if not db_grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    for key, value in grade.model_dump().items():
        setattr(db_grade, key, value)
    db_grade.percentage = (db_grade.marks_obtained / db_grade.total_marks) * 100
    session.add(db_grade)
    session.commit()
    session.refresh(db_grade)
    return db_grade

@router.delete("/grades/{id}")
def delete_grade(id: int, session: Session = Depends(get_session)):
    grade = session.get(Grade, id)
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    session.delete(grade)
    session.commit()
    return {"message": "Deleted"}

@router.post("/grades/{id}/study-tips")
def study_tips(id: int, session: Session = Depends(get_session)):
    grade = session.get(Grade, id)
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    tips = get_study_tips(grade.subject, grade.percentage or 0, grade.total_marks)
    return {"tips": tips}

@router.post("/grades/bulk-upload", response_model=BulkUploadResponse)
def bulk_upload(file_path: str = "data.csv", session: Session = Depends(get_session)):
    # Implement pandas reading logic here as per your earlier requirement
    return {"success": 0, "errors": []}