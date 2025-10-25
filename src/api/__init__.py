from fastapi import APIRouter

from src.api.user import users_router
from src.api.auth import auth_router
router = APIRouter()

router.include_router(auth_router, prefix="/api")
router.include_router(users_router, prefix="/api")

__all__ = ["router"]