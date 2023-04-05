import redis

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response



r = redis.StrictRedis(
    host='127.0.0.1',
    port=6379,
    password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81'
)

router = APIRouter(
    prefix='/login',
    tags=['login'],
)

@router.post('/save_sms')
def send_sms(login: str, sms_code: int):
    r.set(login, sms_code)

@router.get('/get_sms')
def send_sms(login: str):
    r.set(login)
    return r