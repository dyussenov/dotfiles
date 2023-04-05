import requests
from models import GetAccessTokenModel

def get_access_token(url, client_id, client_secret):
    request = requests.post(url, )