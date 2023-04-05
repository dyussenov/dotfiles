from fastapi import APIRouter, Depends
from services import SearchService
from models import User, Search_user

router = APIRouter(
    prefix='/manual-search',
    tags=['manual-search']
)


@router.get('/')
async def get_user(
    login: str,
    service: SearchService = Depends()
):
    user = await service.find_user(login)
    return user


@router.get('/users')
async def get_users(
    user_fields: Search_user,
    service: SearchService = Depends()
):
    print(user_fields.dict())
    #users = await service.find_users(user_fields)
    #print(users)
    #return users
    return 200