from pydantic import BaseModel, field_validator
from typing import Optional, List

class GradeCreate(BaseModel):
    student_name: str
    subject: str
    marks_obtained: float
    total_marks: float
    semester: str
    notes: Optional[str] = None

    @field_validator('marks_obtained', 'total_marks')
    @classmethod
    def validate_marks(cls, v):
        if v < 0:
            raise ValueError('Marks cannot be negative')
        return v

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
