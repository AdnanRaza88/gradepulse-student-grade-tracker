from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class Grade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_name: str
    subject: str
    marks_obtained: float
    total_marks: float
    semester: str
    date: str = Field(default_factory=lambda: str(date.today()))
    percentage: Optional[float] = None
    grade: Optional[str] = None
    notes: Optional[str] = None