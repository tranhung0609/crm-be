from typing import Optional
from pydantic import Field, BaseModel

from src.core.models.query_base_model import QueryBaseModel


class Paginator(QueryBaseModel):
    page: int = Field(default=0, title="Số trang bắt đầu từ 0")
    size: int = Field(default=10, title="Số phần từ một trang")
