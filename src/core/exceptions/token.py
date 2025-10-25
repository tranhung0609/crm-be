from starlette.authentication import AuthenticationError

from src.core.exceptions import CustomException


class DecodeTokenException(CustomException):
    code = 400
    error_code = "TOKEN__DECODE_ERROR"
    message = "Lỗi khi decode token"


class ExpiredTokenException(CustomException):
    code = 400
    error_code = "TOKEN__EXPIRE_TOKEN"
    message = "Token hết hạn"


class LoginException(CustomException):
    code = 400
    error_code = "LOGIN_FAIL"
    message = "Thông tin đăng nhập không chính xác. Vui lòng thử lại"


class KeycloakException(CustomException):
    code = 400
    error_code = "THIRD_PARTY_EXCEPTION"
    message = "Không đăng ký được user"


class TokenInvalidate(CustomException, AuthenticationError):
    code = 401
    error_code = "USER__TOKEN_INVALIDATE"
    message = "Token hết hạn"

class RefreshTokenInvalidate(CustomException, AuthenticationError):
    code = 400
    error_code = "USER__REFRESH_TOKEN_INVALIDATE"
    message = "Refresh token hết hạn"