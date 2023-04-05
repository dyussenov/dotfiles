from fastapi import APIRouter
from . import temp_login

router = APIRouter(prefix='/test')
router.include_router(temp_login.router)
