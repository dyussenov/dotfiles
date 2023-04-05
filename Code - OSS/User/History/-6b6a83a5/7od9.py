import requests
import random
from fastapi import APIRouter, Depends

import models
import services
from settings import settings
from pydantic import BaseModel
router = APIRouter(
    prefix='/auth/sms',
    tags=['/auth/sms'],
)

class SMS(BaseModel):
    phone: str
    login: str

@router.post('/')
async def send_sms(
    data: SMS,
    service: services.SmsService = Depends(),
):
    phone = data.phone
    login = data.login
    print(phone, login)
    code = random.randint(100000, 999999)
    params = {
        'code': code,
        'phone': phone
    }

    url = settings.sms_service_url
    res = requests.post(url, params=params)
    await service.save_code(login, phone, code)
    print(res.status_code)
    return 200

@router.get('/get_code')
async def get_code(
    login: str,
    service: services.SmsService = Depends(),
    ):
    res = await service.get_code_by_login(login)
    return res

@router.get('/check_sms')
async def check_code(
    login: str,
    code: int,
    service: services.SmsService = Depends(),
    ):
    res = await service.check_sms_code(login, code)
    if res == None:
        return {'status': 'login does not exists'}
    return {'status': res}
     