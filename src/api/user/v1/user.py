from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/")
async def read_users():
    return [{"username": "user1"}, {"username": "user2"}]