from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    level: int
    theory_text: str
    task_description: str
    text: str
    expected_result: str