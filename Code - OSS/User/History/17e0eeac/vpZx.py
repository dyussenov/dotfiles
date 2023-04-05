from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    id: Optional[str]
    login: str
    phone: str
    role: str
    email: Optional[str]

class RegisterUser(BaseUser):
    password: str

class User(BaseUser):
    password_hash: str
    name: Optional[str]
    surname: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]



class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'

