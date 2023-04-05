from pydantic import BaseModel
from typing import Literal

class User(BaseModel):
    id: str
    username: str
    exp: datetime
    token_type: Literal["access"]