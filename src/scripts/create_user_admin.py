
import asyncio
from src.app.user.services.user import UserService
from src.core.database.mongo_async.mongo_motor_utils import connect_to_mongo
from src.core.config import config
from fastapi import FastAPI
import hashlib
from src.core.database.mongo_async.mongo_motor import db

async def main():
	app = FastAPI()
	await connect_to_mongo(app)
	user_collection = db.mongo_client[config.MONGO_DB_NAME]["users"]
	password_md5 = hashlib.md5("admin123".encode()).hexdigest()
	admin_user = {
		"user_name": "admin",
		"password": password_md5,
		"full_name": "Admin",
		"email": "admin@example.com",
		"is_active": True
	}
	await user_collection.insert_one(admin_user)
	print("Admin user created!")

if __name__ == "__main__":
	asyncio.run(main())
