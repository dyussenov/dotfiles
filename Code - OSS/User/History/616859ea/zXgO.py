from pydantic import BaseModel
from typing import Optional


class TextFieldBase(BaseModel):
    id: Optional[int]
    field_name: str
    value_ru: str
    value_kz: str

    class Config:
        orm_mode = True

