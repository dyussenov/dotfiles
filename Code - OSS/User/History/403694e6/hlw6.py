import redis
import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

import services
from api import router
from config import settings
from connection_manager import ConnectionManager

app = FastAPI(
    title='Regex Racing',
    docs_url="/",
    description='CodeQuest Regex Recing game microservice',
    version='1.0.0',
)

#origins = settings.ALLOWED_HOSTS.split(',')
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


register_tortoise(
    app,
    db_url="sqlite://database/db.sqlite3",
    modules={"models": ["database.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
    )


app.include_router(router)

manager = ConnectionManager()

@app.websocket("/lobby/{lobby_id}/ws")
async def websocket_endpoint(
    *,
    lobby_id: str,
    token: str,
    websocket: WebSocket,
):  
    #await websocket.accept()
    await manager.connect(websocket)
    lobby_data = services.connect_to_lobby(lobby_id, services.get_current_user(token))
    print(lobby_data)
    await manager.broadcast(json.dumps(lobby_data))
    try:
        while True:
            lobby_data = services.connect_to_lobby(lobby_id, services.get_current_user(token))
    
            data = await websocket.receive_json()
            await manager.broadcast('start game!')

    except WebSocketDisconnect:
        print('qwer')
        manager.disconnect(websocket)
