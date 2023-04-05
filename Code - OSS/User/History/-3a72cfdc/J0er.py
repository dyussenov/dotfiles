from pydantic import BaseModel
from typing import Optional

class BaseUser(BaseModel):
    login: str
    password_hash: str
    phone: str
    role: str


class User(BaseUser):
    id: Optional[str]
    role: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]
