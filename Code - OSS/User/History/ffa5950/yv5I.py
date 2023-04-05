import redis

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response



r = redis.StrictRedis(
    host='redis-17449.c55.eu-central-1-1.ec2.cloud.redislabs.com',
    port=17449,
    password='qwerty'
)

router = APIRouter(
    prefix='/login',
    tags=['login'],
)

@router.post('/save_sms')
def send_sms(code: int, phone: str):
    params = {
        'login': settings.smsc_login,
        'psw': settings.smsc_password,
        'phones': phone,
        'mes': f'{settings.sms_text}\n{code}'
    }
    res = requests.get(settings.smsc_url, params=params)
    return res.status_code