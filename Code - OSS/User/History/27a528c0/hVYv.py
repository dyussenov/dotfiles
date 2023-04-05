from fastapi import APIRouter
from models import Task


router = APIRouter(
    prefix='/learn',
    tags=["learn"]
)

@router.post("/{level}", tags=["learn"])
async def validate_answer(level: int):
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/", tags=["learn"])
async def get_tasks() -> list[Task]:
    return [
        Task(level = 1, theory_text='a',task_description='b',text='c',expected_result='d'),
        Task(level = 2, theory_text='a',task_description='b',text='c',expected_result='d'),
        Task(level = 3, theory_text='a',task_description='b',text='c',expected_result='d'),
    ]