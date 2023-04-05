from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
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


class Search_user(BaseModel):
    login: Optional[str]
    phone: Optional[str]
    role: Optional[str]
    email: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    description: Optional[str]
    gender: Optional[str]
    qualification: Optional[str]
    iin: Optional[int]