from fastapi import APIRouter

from .matchmaker import router as matchmaker_router
from .learn import router as learn_router

router = APIRouter(
    prefix='/regex-race',
)

router.include_router(matchmaker_router)
router.include_router(learn_router)