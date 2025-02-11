from ..model import *
from db import get_session
from ..model.data_model import *
from fastapi import Depends
from util.tool import now
from ..model.dto import UserDTO
from sqlalchemy import and_

class UserRepository:
    def __init__(self):
        self.session = next(get_session())

    def set_login(self, user_id: int):
        """
        用户登录时更新必要信息
        :param user_id: 用户ID
        """
        try:
            last_login = now()
            self.session.query(User).filter(User.id == user_id).update({"last_login": last_login})
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def create_user(self, user: UserDTO):
        """
        创建用户
        :param user: 用户信息
        """
        try:
            _ = User(
                username=user.username,
                email=user.email,
                password=user.password,
                created_at=now(),
                update_at=now()
            )
            self.session.add(_)
            self.session.commit()
            return user
        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_user_by_conditions(self, **conditions):
        """
        根据条件查询用户
        :param conditions: 查询条件
        """
        try:
            # 构建动态的过滤条件
            filters = [getattr(User, key) == value for key, value in conditions.items()]
            user = self.session.query(User).filter(and_(*filters)).first()
            return user
        except Exception as e:
            raise e

    def update_user(self, user: User):
        """
        更新用户信息
        :param user: 用户信息
        """
        try:
            # 将 User 对象的字段转换为字典
            user_dict = {field: getattr(user, field) for field in user.__table__.columns.keys()}
            
            # 过滤掉值为 None 的字段
            user_dict = {k: v for k, v in user_dict.items() if v is not None}
            
            # 更新数据库记录
            self.session.query(User).filter(User.id == user.id).update(user_dict)
            self.session.commit()
            return user
        except Exception as e:
            self.session.rollback()
            raise e
        
    def delete_user(self, user_id: int):
        """
        删除用户
        :param user_id: 用户ID
        """
        try:
            self.session.query(User).filter(User.id == user_id).delete()
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_user_list(self, page: int = 1, page_size: int = 10):
        """
        获取用户列表，支持分页功能
        :param page: 当前页码，默认为1
        :param page_size: 每页显示的记录数，默认为10
        :return: 用户列表
        """
        try:
            # 计算 offset 和 limit
            offset = (page - 1) * page_size
            limit = page_size

            # 查询用户列表
            users = self.session.query(User).offset(offset).limit(limit).all()

            # 查询总记录数
            total_count = self.session.query(User).count()

            # 返回分页结果
            return {
                "users": users,
                "total_count": total_count,
                "page": page,
                "page_size": page_size
            }
        except Exception as e:
            raise e