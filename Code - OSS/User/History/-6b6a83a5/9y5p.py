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
    #requests.post(url, params=params)
    await service.save_code(login, phone, code)
    return

@router.get('/get_code')
async def get_code(
    login: str,
    service: services.SmsService = Depends(),
    ):
    res = await service.get_code_by_login(login)
    return res

@router.get('/check_sms')
async def get_code(
    login: str,
    service: services.SmsService = Depends(),
    ):
    await service.check_sms_code(login)