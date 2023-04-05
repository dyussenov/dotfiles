from fastapi import APIRouter, Depends
import .services
from ..models import User

router = APIRouter(
    prefix='/manual-search',
    tags=['manual-search']
)


@router.get('/', response_model=User)
async def get_user(
    login: str,
    service: SearchService = Depends()
) -> dict:
    user = await service.find_user(login)
    return user


@router.get('/users', response_model=list[User])
async def get_users(
    tags: str,
    service: SearchService = Depends()
):
    users = await service.find_users(tags.split(','))
    print(users)
    return users
