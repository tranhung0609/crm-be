from typing import List
from src.core.database.mongo_async.mongo_motor import db, db1
from src.app.user.models.user import User
from src.core.config import config
from src.core.enums.collection_name import Collections

class UserRepository:
    @staticmethod
    async def get_by_user_id(id: str) -> User:
        doc = await db.mongo_client[config.MONGO_DB_NAME][Collections.USER.value].find_one({
            'user_name': id,
            'owner_id': 'TRANG_NGUYEN'
        }, {'_id': 0})

        return User(**doc) if doc else None