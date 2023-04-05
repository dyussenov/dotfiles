from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    login: str
    phone: str
    role: str
    
class RegisterUser(BaseUser):
    password: str
    code: int
    password_hash: Optional[str]

class SignInUser(BaseModel):
    login: str
    password: str

class User(BaseUser):
    id: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]
    comments: Optional[list[str]]
    school: Optional[str]
    iin: Optional[int]
    
class UpdateUser(BaseModel):
    login: Optional[str]
    phone: Optional[str]
    role: Optional[str]
    email: Optional[str]
    password_hash: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    third_name: Optional[str]
    price: Optional[int]
    education_form: Optional[str]
    price: Optional[int]
    tg_login: Optional[str]
    grade: Optional[int]
    work_time: Optional[int]
    birthday: Optional[str]
    description: Optional[str]
    gender: Optional[str]
    spec: Optional[str]
    subject: Optional[str]
    comments: Optional[list[str]]
    school: Optional[str]
    iin: Optional[int]

class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'

