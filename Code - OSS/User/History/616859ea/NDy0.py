from pydantic import BaseModel
from typing import Optional


class TextFieldBase(BaseModel):
    id: Optional[int]
    field_name: str
    field_value_ru: str
    field_value_kz: str

    class Config:
        orm_mode = True

