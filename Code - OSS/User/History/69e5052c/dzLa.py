from pydantic import BaseModel

class SendSMSBase(BaseModel):
    phone: str
    code: int