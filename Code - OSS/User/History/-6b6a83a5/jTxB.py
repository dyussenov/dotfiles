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
    login: str
):
    params = {
        'code': random.randint(100000, 999999),
        'phone': phone
    }
    url = settings.sms_service_url+'/send_sms'
    print(url)
    requests.post(url, json=params)