from fastapi import APIRouter

from .matchmaker import router as matchmaker_router

router = APIRouter(
    prefix='/regex-race',
)

router.include_router(matchmaker_router)