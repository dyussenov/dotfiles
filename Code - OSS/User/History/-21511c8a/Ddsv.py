import random
import string
#from jose import jwt, JWTError
import jwt
from fastapi import status, HTTPException, Depends
from pydantic import ValidationError

import models
from config import settings


def generate_lobby_id(length: int) -> str:
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str

def get_current_user(token: str):
    return MultiplayerService.validate_token(token)

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
        #try:
        payload = jwt.decode(
            token=token,
            key=settings.JWT_SECRET_KEY,
            algorithms=['HS256']
        )
        #except:
        #    raise exception from None

        user_data = payload.get('user')

        try:
            user = models.User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    def generate_lobby_id(length: int) -> str:
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        return result_str
