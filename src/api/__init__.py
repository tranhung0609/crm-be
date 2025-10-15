from fastapi import APIRouter

from src.api.user import users_router

router = APIRouter()

router.include_router(users_router, prefix="/api")

__all__ = ["router"]