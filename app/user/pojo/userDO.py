"""
数据库的表与类对应
"""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from db.init import Base
from .__init__ import *


class UserDO(Base):
    """
    用户信息表
    """
    __tablename__ = 'user'

    id = Column("id", Integer, primary_key=True, comment='用户唯一id')
    username = Column("username", String(50), nullable=False, comment='用户名称')
    password = Column("password", String(50), nullable=False, comment='用户密码')
    email = Column("email", String(50), comment='用户邮箱')
    create_at = Column("create_at", DateTime, nullable=False, default=datetime.now, comment='用户创建时间')
    update_at = Column("update_at", DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='用户信息最近更新时间')
    last_login = Column("last_login", DateTime, nullable=False, comment='用户上次登录时间')
    role = Column("role", Integer, ForeignKey('role.role_id'), nullable=False, default=1, comment='用户角色')


class RoleDO(Base):
    """
    权限信息表
    """
    __tablename__ = 'role'

    role_id = Column("role_id", Integer, primary_key=True, comment='角色id')
    name = Column("role_name", String(50), nullable=False, comment='角色名称')


class RoleUpgradeRequestDO(Base):
    """
    角色升级申请表
    """
    __tablename__ = 'role_upgrade_request'

    id = Column("id", Integer, primary_key=True, comment='角色升级申请唯一id')
    user_id = Column("user_id", Integer, ForeignKey('user.id'), nullable=False, comment='申请人的id')
    request_role_id = Column("request_role_id", Integer, ForeignKey('role.id'), nullable=False, comment='申请角色')
    status = Column("status", Integer, nullable=False, default=-1, comment='申请状态 -1 未审核 0 审核失败 1 审核通过')
    request_time = Column("request_time", DateTime, nullable=False, default=datetime.now, comment='申请时间')
    approved_by = Column("approved_by", Integer, ForeignKey('user.id'), comment='申请审批通过人')
    request_reason = Column('request_reason', String(100), comment='申请原因')

