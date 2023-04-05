from fastapi import APIRouter

from .matchmaker import router as matchmaker_router
from .singleplayer import router as singleplayer_router

router = APIRouter(
    prefix='/regex-race',
)

router.include_router(matchmaker_router)
router.include_router(singleplayer_router)