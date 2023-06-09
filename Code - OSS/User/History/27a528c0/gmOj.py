from fastapi import APIRouter, Form
from typing import Annotated
from database import Task as TaskModel

import services
from models import Task, TaskResponse

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
async def validate_answer(level: int, regex: Annotated[str, Form()],) -> TaskResponse:
    task = await TaskModel.get(level=level)
    result = services.check_regex(task.text, regex, task.expected_result)
    if result[0]:
        return TaskResponse(is_true=True, result=result[1])
    else:
        return TaskResponse(is_true=False, result=result[1])

@router.get("/", tags=["learn"])
async def get_tasks() -> list[Task]:
    return await TaskModel.all().limit(5)