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
    ) -> models.User:
    token = request.headers['authorization'].split(" ")[1]
    user = service.validate_token(token)
    return user

@router.get("/{lobby}", tags=["lobby"])
async def get_lobby(lobby: str):
    return {"lobby": lobby}