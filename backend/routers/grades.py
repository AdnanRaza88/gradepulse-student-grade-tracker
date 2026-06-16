from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from backend.models import Grade
from backend.schemas import GradeCreate, GradeResponse
from backend.database import get_session
from backend.ai.groq_client import get_study_tips, get_daily_routine
from typing import List

router = APIRouter()

@router.post("/grades/", response_model=GradeResponse)
def create_grade(grade: GradeCreate, session: Session = Depends(get_session)):
    db_grade = Grade(**grade.model_dump())
    db_grade.percentage = round((db_grade.marks_obtained / db_grade.total_marks) * 100, 2)
    
    if db_grade.percentage >= 90:
        db_grade.grade = "A"
    elif db_grade.percentage >= 75:
        db_grade.grade = "B"
    elif db_grade.percentage >= 60:
        db_grade.grade = "C"
    else:
        db_grade.grade = "F"
    
    session.add(db_grade)
    session.commit()
    session.refresh(db_grade)
    return db_grade

@router.get("/grades/", response_model=List[GradeResponse])
def get_all_grades(session: Session = Depends(get_session)):
    return session.exec(select(Grade)).all()

@router.get("/grades/{grade_id}", response_model=GradeResponse)
def get_grade(grade_id: int, session: Session = Depends(get_session)):
    grade = session.get(Grade, grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail="Grade record not found")
    return grade

@router.post("/grades/{grade_id}/study-tips")
def get_study_tips_endpoint(grade_id: int, session: Session = Depends(get_session)):
    grade = session.get(Grade, grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail="Grade record not found")
    
    tips = get_study_tips(grade.subject, grade.percentage or 0, grade.total_marks)
    routine = get_daily_routine(grade.subject, grade.percentage or 0)
    return {"tips": tips, "routine": routine}
