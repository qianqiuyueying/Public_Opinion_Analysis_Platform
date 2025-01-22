from abc import ABC, abstractmethod
from typing import List

from .pojo.userDO import *
from .pojo.userDTO import *

from fastapi import Depends

from .userMapper import UserMapper


class UserService(ABC):
    def __init__(self, userMapper: UserMapper = Depends(UserMapper)):
        self.userMapper = userMapper

    @staticmethod
    def get_user_mapper() -> UserMapper:
        pass

    @abstractmethod
    def login(self, user: UserDTO) -> bool:
        """
        登录方法
        :param user: 用户信息
        :return: 陈公公或失败
        """
        pass

    @abstractmethod
    def logout(self, user: UserDTO) -> bool:
        """
        登出方法
        :param user: 用户信息
        :return: 成功或失败
        """
        pass

    @abstractmethod
    def register(self, user: UserDTO) -> bool:
        """
        注册方法
        :param user: 用户信息
        :return: 注册成功或失败
        """
        pass

    @abstractmethod
    def get_user_info(self, user: UserDTO = Depends()) -> UserDO:
        """
        条件查询用户信息
        :param user: 查询用户信息
        :return:
        """
        pass


    @abstractmethod
    def update_user_info(self, user: UserDTO) -> bool:
        """
        更新角色信息
        :param user: 用户信息
        :return:
        """
        pass

    @abstractmethod
    def get_user_list(self, page: int, page_size: int) -> List[UserDO]:
        """
        分页查看用户信息
        :param page: 页数
        :param page_size: 页面大小
        :return: 角色信息列表
        """
        pass

    @abstractmethod
    def role_upgrade_request(self, request: RoleUpgradeRequestDTO) -> bool:
        """
        角色升级申请
        :param request: 升级申请
        :return: 申请是否创建成功
        """
        pass


