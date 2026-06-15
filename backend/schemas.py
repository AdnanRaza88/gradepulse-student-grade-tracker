from pydantic import BaseModel
from typing import Optional, List

class GradeCreate(BaseModel):
    student_name: str
    subject: str
    marks_obtained: float
    total_marks: float
    semester: str
    notes: Optional[str] = None

class GradeResponse(BaseModel):
    id: int
    student_name: str
    subject: str
    marks_obtained: float
    total_marks: float
    semester: str
    date: str
    percentage: Optional[float]
    grade: Optional[str]
    notes: Optional[str]

class BulkUploadResponse(BaseModel):
    success: int
    errors: List[str]