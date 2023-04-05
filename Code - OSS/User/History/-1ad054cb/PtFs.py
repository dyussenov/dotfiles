from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('/')
async def get_users():
    return 200