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
def send_sms(): #code: int, phone: str
    print(settings.__dict__)