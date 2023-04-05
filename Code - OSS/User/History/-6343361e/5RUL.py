from fastapi import APIRouter
from .user_search import router as user_search_router

router = APIRouter()
router.include_router(user_search_router)