import requests

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

from settings import settings

from models import SendSMSBase

router = APIRouter(
    prefix='/notification',
    tags=['notification'],
)

@router.post('/send_sms')
def send_sms(data: SendSMSBase):
    code = data.code
    phone = data.phone
    params = {
        'login': settings.smsc_login,
        'psw': settings.smsc_password,
        'phones': phone,
        'mes': f'{settings.sms_text}\n{code}'
    }
    res = requests.get(settings.smsc_url, params=params)
    return res.status_code