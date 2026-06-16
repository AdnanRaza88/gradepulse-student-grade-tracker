from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class Grade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_name: str = Field(index=True, min_length=1)
    subject: str = Field(index=True, min_length=1)
    marks_obtained: float = Field(ge=0)
    total_marks: float = Field(gt=0)
    semester: str = Field(min_length=1)
    date: str = Field(default_factory=lambda: str(date.today()))
    percentage: Optional[float] = None
    grade: Optional[str] = None
    notes: Optional[str] = None
