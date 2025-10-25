from urllib import request
from fastapi import APIRouter, Request
from src.app.user.schemas.user import UserCreateRequest
from src.core.exceptions.user import UserNotFoundException
from src.app.user.services.user import UserService

user_router = APIRouter()

@user_router.get("",
                 status_code=200,
                 response_model_exclude_none=True)
async def get_users(request: Request):
    print(f"Request : {request}")
    print("Headers:", dict(request.headers))
    print("Method:", request.method)
    print("URL:", str(request.url))
    print("Query params:", dict(request.query_params))
    print("Client:", request.client)
    if not request.user:
        raise UserNotFoundException
    # result = await UserService.get_users(request)
    # return result

@user_router.post("", 
                  status_code=200, 
                  response_model_exclude_none=True)
async def create_user(params: UserCreateRequest, request: Request):
    if not request.user:
        raise UserNotFoundException
    result = await UserService.create_user(params, request) 