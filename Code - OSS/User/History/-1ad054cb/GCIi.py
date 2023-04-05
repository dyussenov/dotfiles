from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/users',
    tags=['users'],
)