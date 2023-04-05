from pydantic import BaseModel
from typing import Optional
from bson.objectid import ObjectId


class BaseUser(BaseModel):
    id: str
    login: str
    password_hash: str
    phone: str
    role: str


class User(BaseUser):
    role: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]
