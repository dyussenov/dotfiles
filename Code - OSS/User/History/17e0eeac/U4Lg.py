from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    id: Optional[str]
    login: str
    password_hash: str
    phone: str
    role: str

class User(BaseUser):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]



class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'

