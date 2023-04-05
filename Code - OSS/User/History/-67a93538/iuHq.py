from fastapi import APIRouter, Depends, Request
from database import models
#from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/customers',
    tags=['customers'],
)


@router.get('')
async def get_customers():
    return 200


@router.get('/{id}')
async def get_customer_by_id():
    return 200


@router.post('', response_model=models.Customer)
async def add_customer(customer: models.AddCustomer):
    return customer