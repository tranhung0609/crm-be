from datetime import datetime
from typing import Optional, List
from pydantic import Field
from app import BaseEntity
from src.core.utils.utils import get_timestamp_utc

class User(BaseEntity):
    user_id: Optional[str] = Field(title="Mã người dùng")
    user_name: Optional[str] = Field(title="Tên người dùng")
    email: Optional[str] = Field(title="Email người dùng")
    full_name: Optional[str] = Field(title="Họ và tên người dùng")
    address: Optional[str] = Field(title="Địa chỉ người dùng")
    phone: Optional[str] = Field(title="Số điện thoại người dùng")
    is_active: Optional[bool] = Field(default=True, title="Trạng thái hoạt động của người dùng")
    start_date: Optional[int] = Field(default=int(get_timestamp_utc()), title="Thời gian nhận việc")
    end_date: Optional[int] = Field(title="Thời gian nghỉ việc")
    probation_end_date: Optional[int] = Field(title="Thời gian kết thúc thử việc")
    department: Optional[str] = Field(title="Bộ phận")
    position: Optional[str] = Field(title="Chức vụ")
    salary: Optional[float] = Field(title="Mức lương")
    avatar: Optional[str] = Field(title="Ảnh đại diện người dùng")
    gender: Optional[str] = Field(title="Giới tính người dùng")
    date_of_birth: Optional[int] = Field(title="Ngày sinh người dùng")
    password_hash: Optional[str] = Field(title="Mật khẩu đã băm")
    