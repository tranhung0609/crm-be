from time import time
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
import hashlib
import jwt
from src.core.config import config
from src.core.database.mongo_async.mongo_motor import db

auth_route = APIRouter()

class LoginRequest(BaseModel):  
	user_name: str
	password: str

@auth_route.post("/login")
async def login(request_data: LoginRequest):
	user_collection = db.mongo_client[config.MONGO_DB_NAME]["users"]
	user = await user_collection.find_one({"user_name": request_data.user_name})
	if not user:
		raise HTTPException(status_code=401, detail="User not found")
	password_md5 = hashlib.md5(request_data.password.encode()).hexdigest()
	if user.get("password") != password_md5:
		raise HTTPException(status_code=401, detail="Invalid password")
	payload = {
		"user_id": str(user.get("user_id", "")),
		"user_name": user["user_name"]
	}
	token = jwt.encode(payload, config.JWT_SECRET_KEY, algorithm="HS512")
	return {"access_token": token}
