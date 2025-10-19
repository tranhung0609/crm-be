from typing import Optional
from pydantic import BaseModel, Field
from src.core.utils.utils import get_timestamp_utc


class BaseEntity(BaseModel):
    owner_id: Optional[str] = Field(title="Thuộc hệ thống của chủ sở hữu nào")
    log_created_user_id: Optional[str] = Field(title="Tài khoản tạo ra bản ghi này")
    log_updated_user_id: Optional[str] = Field(title="Tài khoản update bản ghi này")
    log_deleted_user_id: Optional[str] = Field(title="Tài khoản xóa bản ghi này")
    log_created_time: Optional[int] = Field(default=int(get_timestamp_utc()),
                                            title="thời điểm tạo bản ghi này lưu milisecord")
    log_updated_time: Optional[int] = Field(default=int(get_timestamp_utc()),
                                            title="Thời điểm update bản ghi này milisecord")
    log_deleted_time: Optional[int] = Field(title="Thời điểm xóa bản ghi này milisecord")
    log_is_deleted: Optional[int] = Field(default=0,
                                          title="Trạng thái xóa bản ghi 0: Bản ghi hiện hành; 1: Bản ghi đã bị xóa")
    log_updated_info: Optional[str] = Field(title="Tài khoản tạo ra bản ghi này")
    log_deleted_info: Optional[str] = Field(title="Tài khoản tạo ra bản ghi này")
