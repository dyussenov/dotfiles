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
def send_sms(code: int, phone: str):
    params = {
        'login': settings.smsc_login,
        'psw': settings.smsc_password,
        'phones': phone,
        'mes': f'{settings.sms_text}\n{code}'
    }
    res = requests.get(settings.smsc_url, params=params)
    return res.status_code

@router.post('/test_sms')
def send_sms():
    params = {
        'login': settings.smsc_login,
        'psw': settings.smsc_password,
        'phones': '+77765187501',
        'mes': f'{settings.sms_text}\n{1234}'
    }
    res = requests.get(settings.smsc_url, params=params)
    return res.status_code