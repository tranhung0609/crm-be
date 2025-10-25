from src.core.utils.utils import is_blank
from src.core.exceptions.user import UserNameException, UserEmailException, UserNameInvalidException
from src.core.utils.validate import validate_username
from src.core.config import config
from src.core.database.mongo_async.mongo_motor import db
class UserService:


    @staticmethod
    async def get_users(request):
        user_collection = db.mongo_client[config.MONGO_DB_NAME]["users"]
        users = await user_collection.find({"is_active": True}).to_list(length=None)
        return users

    @staticmethod
    async def create_user(params, current_user, request):
        if is_blank(params.user_name):
            raise UserNameException
        if is_blank(params.email):
            raise UserEmailException
        if not validate_username(username=params.user_name):
            raise UserNameInvalidException