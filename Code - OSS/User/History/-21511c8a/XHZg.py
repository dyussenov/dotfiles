import random
import string

import jwt
from fastapi import status, HTTPException, Depends
from pydantic import ValidationError

import models
from config import settings
from redis_db import redis_db


def generate_lobby_id(length: int) -> str:
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str

def get_current_user(token: str):
    return MultiplayerService.validate_token(token)

def create_lobby(lobby_id: str, user: models.User):
    redis_db.hmset(lobby_id, {'creator': user.username})

def stringify_dict(bstring_dict):
    res = {}
    for k,v in bstring_dict.items():
        res[k.decode("utf-8") ]=v.decode("utf-8") 
    return res

def connect_to_lobby(lobby_id: str, user: models.User):
    lobby = redis_db.hgetall(lobby_id)
    print(lobby.values())
    #if b'creator' in lobby.keys():
    if lobby[b'creator'].decode("utf-8") != user.username and bytes(user.username, 'utf-8') not in lobby.values():
        lobby[len(lobby.keys())] = user.username
        redis_db.hmset(lobby_id, lobby)

    return {'users': stringify_dict(redis_db.hgetall(lobby_id))}


def get_lobby(lobby_id: str):
    res = redis_db.hgetall(lobby_id)
    return res



class MultiplayerService():

    @classmethod
    def validate_token(cls, token: str):
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='could not authorize credentials',
            headers={
                'WWW-authenticate': 'Bearer'
            },
        )
        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=['HS256']
            )
        except jwt.exceptions.InvalidSignatureError:
            raise exception from None

        try:
            user = models.User.parse_obj(payload)
        except ValidationError:
            raise exception from None

        return user
