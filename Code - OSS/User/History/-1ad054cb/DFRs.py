from fastapi import APIRouter, Depends, Request
#from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('')
async def get_users():
    return 200


@router.get('/{id}')
async def get_user_by_id():
    return 200

@router.post('')
async def add_user():
    return 200