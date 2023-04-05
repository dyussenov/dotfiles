from fastapi import APIRouter, Depends
from services import SearchService
from models import User

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


@router.get('/users', response_model=list[User])
async def get_users(
    user_fields: S,
    service: SearchService = Depends()
):
    users = await service.find_users(tags.split(','))
    print(users)
    return users
