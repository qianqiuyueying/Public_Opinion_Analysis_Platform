"""
前端请求后端DTO接收
"""
from pydantic import BaseModel
from typing import Optional


class UserDTO(BaseModel):
    username: str
    password: str
    email: Optional[str] = None

    # 这个配置允许orm对象转化为pydantic对象
    class Config:
        from_attributes = True


class RoleUpgradeRequestDTO(BaseModel):
    user_id: int
    request_role_id: int
    status: int
    request_reason: Optional[str] = None

    class Config:
        from_attributes = True
