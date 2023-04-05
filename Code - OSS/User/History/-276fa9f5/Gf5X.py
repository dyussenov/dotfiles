from fastapi import APIRouter

router = APIRouter(
    prefix='/lobby',
)

@router.post("/", tags=["lobby"])
async def create_lobby():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/{lobby}", tags=["lobby"])
async def get_lobby(lobby: str):
    return {"lobby": lobby}