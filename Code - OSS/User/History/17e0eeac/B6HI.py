from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    id: Optional[str]
    login: str
    phone: str
    role: str
    email: Optional[str]
    password_hash: Optional[str]
    
class RegisterUser(BaseUser):
    password: str
    code: int

class SignInUser(BaseModel):
    login: str
    password: str

class User(BaseUser):
    name: Optional[str]
    surname: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]
    comments: Optional[list[str]]
    school: Optional[str]
    iin: Optional[int]

class UpdateUser(BaseModel):
    id: Optional[str]
    login: Optional[str]
    phone: Optional[str]
    role: Optional[str]
    email: Optional[str]
    password_hash: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]
    comments: Optional[list[str]]
    school: Optional[str]
    iin: Optional[int]

class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'

