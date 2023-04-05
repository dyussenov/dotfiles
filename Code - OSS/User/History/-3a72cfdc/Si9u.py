from pydantic import BaseModel
from typing import Optional



class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")


class BaseUser(BaseModel):
    _id: str
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
