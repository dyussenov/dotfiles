from fastapi import APIRouter

from .users import router as users_router
from .courses import router as courses_router
from .lessons import router as lessons_router
from .sms import router as sms_router

router = APIRouter()
router.include_router(users_router)
router.include_router(courses_router)
router.include_router(lessons_router)
router.include_router(sms_router)
