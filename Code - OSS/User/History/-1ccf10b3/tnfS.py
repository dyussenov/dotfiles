from fastapi import APIRouter
from . import sms_api

router = APIRouter(prefix='/sms')
router.include_router(module.router)
