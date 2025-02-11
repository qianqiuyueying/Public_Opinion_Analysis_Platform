from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserDTO(BaseModel):
    """
    user表的数据传输对象
    """
    username: str  # 必填字段
    email: Optional[str] = None    # 非必填字段
    code: Optional[int] = None    # 非必填字段
    password: str # 必填字段
    avatar: Optional[str] = None  # 非必填字段
    role: Optional[int] = 0                # 非必填字段，有默认值
    last_login: Optional[str] = None  # 非必填字段
    created_at: Optional[str] = None  # 非必填字段
    update_at: Optional[str] = None  # 非必填字段

    model_config = ConfigDict(from_attributes=True)

class EmailDTO(BaseModel):
    email: str  # 必填字段

    model_config = ConfigDict(from_attributes=True)