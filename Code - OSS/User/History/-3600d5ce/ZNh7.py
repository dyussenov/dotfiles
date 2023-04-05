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
def send_sms(code: str, phone: str):

    params = {
        'recipient': phone,
        'apiKey': settings.api_key,
        'from': sender,
        'text': f'{settings.sms_text}: {code}'
    }
    res = requests.get(settings.smsc_url, params=params)
    return 200