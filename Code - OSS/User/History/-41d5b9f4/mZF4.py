from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

import models
import services

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/sign-up', response_description="User data added into the database")
async def add_user_data(
        new_user: models.RegisterUser,
        service: services.AuthService = Depends()
    ):  
    if service.validate_sms(new_user.login, new_user.code, new_user.phone):
        return await service.register_new_user(new_user)
    else:
        return 204

@router.post('/sign-in', response_model=models.Token)
async def sign_in(
        data: models.SignInUser,
        service: services.AuthService = Depends(),
    ):
    return await service.authenticate_user(
        data.login,
        data.password
    )


@router.get(
    '/user/',
    )
async def get_user(
    r: Request,
    service: services.AuthService = Depends()
    ):
    print(r.headers)
    token = r.headers['authorization'].split(" ")[1]
    login = services.get_current_user(token).login
    print(login)
    return await service.find_user(login)

@router.put(
    '/user/',
    description='add tags after registration'
)
async def update_user(
        updating: models.UpdateUser,
        r: Request,
        service: services.AuthService = Depends()
):
    token = r.headers['authorization'].split(" ")[1]
    return await service.update_user(services.get_current_user(token), updating)




