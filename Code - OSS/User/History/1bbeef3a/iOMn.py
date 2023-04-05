import time
import requests

from models import GetAccessTokenModel
from database import redis_db


def get_access_token(url, client_id, client_secret):
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    request = requests.post(url, data=payload)
    return request.json()

def send_sms(url, access_token, text, phone, code):
    sms_text = text + ': ' + code
    headers = {
        'Authorization': 'Bearer '+ access_token
    }
    payload = {
        'sender': 'workaus.kz',
        'phones': [phone],
        'body': sms_text,
        'transliterate': 1,
    }
    print(payload)
    request = requests.post(url, headers=headers, json=payload)
    return request.json()

async def get_access_token_from_db():
    token = redis_db.hmget('access_token', ['token', 'timestamp'])
    return token

async def set_access_token(token):
    redis_db.hmset('access_token', {'token': token, 'timestamp': time.time()})

