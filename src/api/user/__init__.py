from fastapi import APIRouter

from src.api.user.v1.user import user_router

users_router = APIRouter()
users_router.include_router(user_router, prefix="/v1/users", tags=["User"])

__all__ = ["users_router"]
