from pydantic import BaseModel

class SendSMSBase(BaseModel):
    phone: str
    code: int

class GetAccessTokenModel(BaseModel):
    grant_type: str = "client_credentials"
    client_id: str
    client_secret: str