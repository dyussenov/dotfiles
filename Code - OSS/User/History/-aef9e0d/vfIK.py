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
    gender: str = None,
    education_form: str = None,
    subject: str = None,
    grade: int = None,
    service: SearchService = Depends()
):
    user_fields = {
        'gender': gender,
        'education_form': education_form,
        'subject': subject,
        'grade': grade
    }
    users = await service.find_users(user_fields.dict())
    return users