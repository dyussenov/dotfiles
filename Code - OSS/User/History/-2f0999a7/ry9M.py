from pydantic import BaseModel
from typing import Optional


class LessonBase(BaseModel):
    id: Optional[str] = None
    teacher_id: Optional[str] = None
    student_id: Optional[str] = None
    course_id: Optional[str] = None
    lessons_days: Optional[list]