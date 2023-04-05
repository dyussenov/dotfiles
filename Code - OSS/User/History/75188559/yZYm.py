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
async def send_sms():
    r = await oauth_service.get_access_token_from_db()
    print(r)
    ''' url = settings.access_token_url
    client_id = settings.client_id
    client_secret = settings.client_secret
    res = oauth_service.get_access_token(url, client_id, client_secret)
    await oauth_service.set_access_token(res['access_token'])'''
    return 200
