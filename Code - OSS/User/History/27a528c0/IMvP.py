from fastapi import APIRouter

router = APIRouter(
    prefix='/learn',
    tags=["learn"]
)

@router.post("/{level}", tags=["learn"])
async def validate_answer(level: int):
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/", tags=["learn"])
async def get_tasks(level: int):
    return {"level": int}