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
async def get_tasks(level: int) -> list[Task]:
    return [
        Task(1,'a','b', 'c', 'd', 'e'),
        Task(1,'a','b', 'c', 'd', 'e'),
        Task(1,'a','b', 'c', 'd', 'e'),
    ]