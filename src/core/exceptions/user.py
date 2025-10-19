from src.core.exceptions.base import CustomException


class UserNotFoundException(CustomException):
    code = 404
    error_code = "USER__NOT_FOUND"
    message = "Không tìm thấy người dùng"
    
class UserNameException(CustomException):
    code = 400
    error_code = "USER__USER_NAME_REQUIRED"
    message = "Tên đăng nhập bắt buộc phải nhập"
    
class UserNameInvalidException(CustomException):
    code = 400
    error_code = "USER__USER_NAME_INVALID"
    message = "Tên đăng nhập không hợp lệ"        

class UserEmailException(CustomException):
    code = 400
    error_code = "USER__EMAIL_REQUIRED"
    message = "Email người dùng bắt buộc phải nhập"