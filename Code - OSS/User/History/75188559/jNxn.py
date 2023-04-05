import time
import requests

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

from settings import settings

from models import SendSMSBase
from services import oauth_service

router = APIRouter(
    prefix='/notification',
    tags=['notification'],
)

@router.post('/send_sms')
async def send_sms(data: SendSMSBase):
    client_id = settings.client_id
    client_secret = settings.client_secret
    access_token_url = settings.access_token_url

    r = await oauth_service.get_access_token_from_db()
    if not r:
        new_token = oauth_service.get_access_token(access_token_url, client_id, client_secret)
        await oauth_service.set_access_token(new_token['access_token'])
        r = await oauth_service.get_access_token_from_db()

    last_timestamp = float(r[1].decode('utf-8'))
    current_time = time.time()
    
    if current_time - last_timestamp >3500:
        url = settings.access_token_url
        
        new_token = oauth_service.get_access_token(url, client_id, client_secret)
        await oauth_service.set_access_token(new_token['access_token'])
        r = await oauth_service.get_access_token_from_db()

    url = settings.sendpulse_base_url
    access_token = r[0].decode('utf-8')
    text = settings.sms_text
    code = data.code
    phone = data.phone
    r = oauth_service.send_sms(url, access_token, text, phone, str(code))
    print(r)
    return 200
