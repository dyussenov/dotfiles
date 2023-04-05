import requests

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

from settings import settings

#import models

router = APIRouter(
    prefix='/notification',
    tags=['notification'],
)

@router.post('/send_sms')
async def send_sms(code: int, phone: str):
    params = {
        'login': settings.smsc_login,
        'psw': settings.smsc_password,
        'phones': phone,
        'mes': settings.sms_text+str(code)
    }
    await requests.get(settings.smsc_url, params=params)
    