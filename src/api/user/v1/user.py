from fastapi import APIRouter, Request
from src.app.user.schemas.user import UserRegisterRequest
from src.core.exceptions.user import UserNotFoundException
from src.app.user.services.user import UserService

user_router = APIRouter()

##đăng ký user
@user_router.post("/create", 
                  status_code=200, 
                  response_model_exclude_none=True)
async def create_user(params: UserRegisterRequest, request: Request):
    if not request.user:
        raise UserNotFoundException
    result = await UserService.create_user(params, request.user, request)