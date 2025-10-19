from src.core.utils.utils import is_blank
from src.core.exceptions.user import UserNameException, UserEmailException, UserNameInvalidException
from src.core.utils.validate import validate_username

class UserService:
    
    @staticmethod
    async def create_user(params, current_user, request):
        if is_blank(params.user_name):
            raise UserNameException
        if is_blank(params.email):
            raise UserEmailException
        if not validate_username(username=params.user_name):
            raise UserNameInvalidException
        
        
        