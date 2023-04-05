from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

#import models

router = APIRouter(
    prefix='/notification',
    tags=['notification'],
)

@router.post('/send')