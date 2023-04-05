import requests
import random
from fastapi import APIRouter, Depends

import models
import services
from settings import settings

router = APIRouter(
    prefix='/sms',
    tags=['sms'],
)

@router.post('/')
async def send_sms(
    phone: str,
    login: str,
    service: services.SmsService = Depends(),
):
    code = random.randint(100000, 999999)
    params = {
        'code': code,
        'phone': phone
    }
    url = settings.sms_service_url
    print(url)
    requests.post(url, params=params)
    service.save_code(login, phone, code)
    return 200