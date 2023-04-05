from datetime import datetime
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

async def set_access_token(token):
    redis_db.hmset('access_token', {'token': token, 'timestamp': datetime.now()})