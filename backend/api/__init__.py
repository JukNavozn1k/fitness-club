from fastapi import APIRouter

from .auth import router as auth_router
from .reviews import router as reviews_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(reviews_router)