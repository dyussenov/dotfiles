from fastapi import APIRouter, Depends
from ..services import SearchService
from ..models import User

router = APIRouter(
    prefix='/user',
    tags=['user']
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

@router.get('/teachers', response_model=list[User])
async def get_all_teachers(
    service: SearchService = Depends()
):
    teachers = await service.get_users('teacher')
    return teachers

@router.get('/students', response_model=list[User])
async def get_all_students(
    service: SearchService = Depends()
):
    students = await service.get_users('students')
    return students

@router.get('/{user_id}', response_model=User)
async def get_user(
    user_id: str,
    service: SearchService = Depends()
):
    user = await service.get_user(user_id)
    return user


