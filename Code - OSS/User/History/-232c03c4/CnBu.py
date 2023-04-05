from pydantic import BaseModel
from typing import Literal

class User(BaseModel):
    id: str
    username: str
    exp: int
    token_type: Literal["access"]


class CreateLobbyResponse(BaseModel):
    user: User
    lobby_id: str