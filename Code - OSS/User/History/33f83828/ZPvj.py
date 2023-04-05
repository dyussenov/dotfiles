from pydantic import BaseModel

class SendSMSBase(BaseModel):
    phone: str
    login: str