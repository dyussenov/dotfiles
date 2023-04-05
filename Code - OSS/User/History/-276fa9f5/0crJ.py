from fastapi import APIRouter, Depends, Request

import models
import services

router = APIRouter(
    prefix='/lobby',
)

@router.post("/", tags=["lobby"])
async def create_lobby(
        request: Request,
        service: services.MultiplayerService = Depends(),
    ) -> models.CreateLobbyResponse:

    lobby_id = services.generate_lobby_id(5)
    token = request.headers['authorization']
    user = service.validate_token(token)
    
    return {'user': user, 'lobby_id': lobby_id}

@router.get("/{lobby}", tags=["lobby"])
async def get_lobby(lobby: str):
    return {"lobby": lobby}