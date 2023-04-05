from fastapi import APIRouter
from sms_api import router as sms_router

router = APIRouter(prefix='/sms')
router.include_router(sms_api.sms_router)
