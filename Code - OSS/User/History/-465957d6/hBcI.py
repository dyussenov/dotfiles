from fastapi import APIRouter

router = APIRouter(
    prefix='/singleplayer',
)

@router.post("/", tags=["singleplayer"])
async def create_lobby():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/{level}", tags=["singleplayer"])
async def get_lobby(lobby: str):
    return {"lobby": lobby}