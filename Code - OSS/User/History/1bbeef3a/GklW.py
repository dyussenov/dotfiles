import requests
from models import GetAccessTokenModel

def get_access_token(url, client_id, client_secret):
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    request = requests.post(url, )