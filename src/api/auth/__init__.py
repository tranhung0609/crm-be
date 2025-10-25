from fastapi import APIRouter

from src.api.auth.v1.auth import auth_route

auth_router = APIRouter()
auth_router.include_router(auth_route, prefix="/v1/auth", tags=["Auth"])

__all__ = ["auth_router"]