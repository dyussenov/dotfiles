from fastapi import APIRouter
from . import text
from . import admin_text
from . import media

router = APIRouter(prefix='/content')
router.include_router(text.router)
router.include_router(admin_text.router)
router.include_router(media.router)
