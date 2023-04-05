from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

@router.get(
    '/{filename}'
)
def get_file():
    

