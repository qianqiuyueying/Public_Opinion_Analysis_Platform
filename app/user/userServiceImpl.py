from .userService import *
from .userMapper import UserMapper
from fastapi import Depends


class  UserServiceImpl(UserService):
    def __int__(self, user_mapper : UserMapper = Depends(UserMapper)):
        self.user_mapper = user_mapper


    def login(self, user: UserDTO) -> bool:
        """
        登陆方法
        :param user: user的必要信息
        :return: 登录是否成功
        """
        pass

    def logout(self, user: UserDTO) -> bool:
        """
        登出方法
        :param user: 目前登陆用户的必要信息
        :return: 登出是否成功
        """
        pass

    def register(self, user: UserDTO) -> bool:
        """
        注册方法
        :param user: 用户的必要信息
        :return: 注册是否成功
        """
        pass

    def get_user_info(self, user: UserDTO = Depends()) -> UserDO:
        """
        获取用户的必要信息
        :param user: 查询用户的条件
        :return: 用户的必要信息
        """
        return self.user_mapper.find_user(user)

    def update_user_info(self, user: UserDTO) -> bool:
        """
        更新用户的信息
        :param user: 查询用户的条件以及更新的信息
        :return: 更新是否成功
        """
        pass

    def get_user_list(self, page: int, page_size: int) -> List[UserDO]:
        """
        分页返回用户列表
        :param page: 页码
        :param page_size: 页面大小
        :return: 用户列表
        """
        pass

    def role_upgrade_request(self, request: RoleUpgradeRequestDTO) -> bool:
        """
        请求升级角色身份
        :param request: 升级请求
        :return: 请求是否建立成功
        """
        pass
