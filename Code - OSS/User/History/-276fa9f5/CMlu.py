from fastapi import APIRouter, Depends, Request, WebSocket

import models
import services
import database

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
    services.create_lobby(lobby_id, user)

    return {'user': user, 'lobby_id': lobby_id}


@router.get("/mp-tasks", tags=["lobby"])
async def get_multiplayer_tasks():
    return await database.MultiplayerTask.all()

@router.get("/{lobby_id}", tags=["lobby"])
async def get_lobby(
    lobby_id: str,
    request: Request,
    service: services.MultiplayerService = Depends(),
    ):
    token = request.headers['authorization']
    user = service.validate_token(token)
    services.connect_to_lobby(lobby_id, user)
    return services.get_lobby(lobby_id)

