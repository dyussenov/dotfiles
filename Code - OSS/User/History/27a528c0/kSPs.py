from fastapi import APIRouter
from database import Task as TaskModel

import services
from models import Task

router = APIRouter(
    prefix='/learn',
    tags=["learn"]
)


@router.post("/", tags=["learn"])
async def add_task(task: Task):
    task = await TaskModel.create(
        title = task.title,
        theory_text = task.theory_text,
        task_description = task.task_description,
        text = task.text,
        expected_result = task.expected_result
    )
    return 200

@router.post("/{level}", tags=["learn"])
async def validate_answer(level: int, regex: Annotated[str, Form()],):
    return services.check_regex()
    

@router.get("/", tags=["learn"])
async def get_tasks() -> list[Task]:
    return await TaskModel.all()