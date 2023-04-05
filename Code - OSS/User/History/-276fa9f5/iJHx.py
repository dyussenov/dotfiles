from fastapi import APIRouter, Depends, Request

import models
import services

router = APIRouter(
    prefix='/lobby',
)

@router.post("/", tags=["lobby"])
async def create_lobby(
    r: Request,
    service: services.AuthService = Depends(),
    ):
    return 200

@router.get("/{lobby}", tags=["lobby"])
async def get_lobby(lobby: str):
    return {"lobby": lobby}