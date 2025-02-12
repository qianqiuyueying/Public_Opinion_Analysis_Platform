from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from db import Base
from datetime import datetime
from enum import Enum as PyEnum

class Role(PyEnum):
    """
    角色枚举
    """
    GUEST = 0 # 游客
    USER = 1 # 用户
    VIP = 2 # VIP
    ADMIN = 3 # 管理员

class User(Base):
    """
    用户信息表
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = Column(String(50), nullable=False, unique=True, comment='用户名')
    avatar = Column(String(200), nullable=True, comment='头像')
    password = Column(String(60), nullable=False, comment='密码')
    email = Column(String(50), nullable=False, unique=True, comment='邮箱')
    created_at = Column(DateTime, nullable=False, default=datetime.now, comment='创建时间')
    update_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    last_login = Column(DateTime, nullable=True, comment='最后登录时间')
    role = Column(Enum(Role), nullable=False, default=Role.GUEST, comment='角色id，0游客1用户2VIP3管理员')


class permission(Base):
    """
    权限表
    """
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    role_id = Column(Integer, nullable=False, comment='角色ID')
    permission_path = Column(String(200), nullable=False, comment='许可路径')
    name = Column(String(50), nullable=False, comment='路径名称')
    created_at = Column(DateTime, nullable=False, default=datetime.now, comment='创建时间')
    update_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')
