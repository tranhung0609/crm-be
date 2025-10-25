from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, EmailStr

from src.app.user.models.user import User
from src.core.utils.utils import get_timestamp_utc
from src.core.models.common import Paginator

class UserCreateRequest(BaseModel):
    user_name: str = Field(..., title="Tên người dùng")
    email: EmailStr = Field(..., title="Email người dùng")
    full_name: Optional[str] = Field(None, title="Họ và tên người dùng")
    address: Optional[str] = Field(None, title="Địa chỉ người dùng")
    phone: Optional[str] = Field(None, title="Số điện thoại người dùng")
    is_active: Optional[bool] = Field(True, title="Trạng thái hoạt động của người dùng")
    start_date: Optional[int] = Field(None, title="Thời gian nhận việc")
    end_date: Optional[int] = Field(None, title="Thời gian nghỉ việc")
    probation_end_date: Optional[int] = Field(None, title="Thời gian kết thúc thử việc")
    department: Optional[str] = Field(None, title="Bộ phận")
    position: Optional[str] = Field(None, title="Chức vụ")
    salary: Optional[float] = Field(None, title="Mức lương")
    avatar: Optional[str] = Field(None, title="Ảnh đại diện người dùng")
    gender: Optional[str] = Field(None, title="Giới tính người dùng")
    date_of_birth: Optional[int] = Field(None, title="Ngày sinh người dùng")
    
    