from db.init import get_session
from .pojo.userDO import *

class UserMapper:

    def create_user(self, user: UserDO) -> bool:
        """
        创建新的用户
        :param user: 用户信息
        :return: 创建是否成功
        """
        with get_session() as session:
            session.add(user)
            session.commit()
            return True

    def delete_user(self, user: UserDO) -> bool:
        """
        删除指定用户
        :param user:
        :return:
        """
        with get_session() as session:
            session.delete(user)
            session.commit()
            return True

    def update_user(self, user: UserDO) -> bool:
        """
        更新用户信息
        :param user: 用户信息
        :return: 是否更新成功
        """
        with get_session() as session:
            session.add(user)
            session.commit()
            return True

    def find_user(self, user: UserDO) -> UserDO:
        """
        查询用户
        :param user: 用户信息
        :return: 用户信息
        """
        with get_session() as session:
            if user.username:
                result = session.query(UserDO).filter(UserDO.username == user.username).first()
                return result
