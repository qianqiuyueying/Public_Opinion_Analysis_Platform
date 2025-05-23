from ..model.dto import *
from ..repository.userRespository import *
from fastapi import HTTPException
from util.tool import *
from rdb import *
from random import randint
from typing import List

class userService:
    """
    用户模块的服务层
    """
    def login(self, user: UserDTO) -> User:
        """
        用户登录
        :param user: 用户信息
        :return: 用户信息
        """
        try:
            # 查询用户信息
            respository = UserRepository()
            user_data = respository.get_user_by_username(user.username)  # 数据库用户信息
            if user_data is None:
                raise HTTPException(status_code=404, detail="用户不存在")
            # 校验密码
            password_manager = PasswordManager()
            password_data_str = user_data.password
            password_data_bytes = password_data_str.encode('utf-8')
            if not password_manager.check_password(password_data_bytes, user.password):
                raise HTTPException(status_code=400, detail="密码错误")
            # 记录登录信息
            respository = UserRepository()
            respository.set_login(user_data.id)
            return user_data
        except Exception as e:
            raise e
        
    def send_verify_code1(self, username: str, email: str) -> None:
        """
        发送验证码
        :param username: 用户名
        :param email: 邮箱地址
        """
        try:    
            # 判断邮箱是否已经注册
            respository = UserRepository()
            if respository.get_user_by_conditions(email=email):
                raise HTTPException(status_code=400, detail="邮箱已注册")
            # 生成验证码
            code = randint(100000, 999999)
            # 发送验证码
            send_verify_code_to_email(username, email, code)
            # 往 Redis 中存储验证码
            store_verify_code(email, code)
        except Exception as e:
            raise e
        
    def register(self, user: UserDTO) -> None:
        """
        用户注册
        :param user: 用户信息
        """
        try:
            # 校验验证码
            code = user.code
            true_code = get_verify_code(user.email)
            # 判断验证码是否存在
            if not true_code:
                raise HTTPException(status_code=400, detail="请重新发送验证码")
            # 判断验证码是否正确
            if code != true_code:
                raise HTTPException(status_code=400, detail="验证码错误")
            # 判断用户是否存在
            respository = UserRepository()
            if respository.get_user_by_username(user.username) is not None:
                raise HTTPException(status_code=400, detail="用户已存在")
            # 判断邮箱是否已经注册
            if respository.get_user_by_conditions(email=user.email):
                raise HTTPException(status_code=400, detail="邮箱已注册")
            # hash 密码
            password_manager = PasswordManager()
            user.password = password_manager.hash_password(user.password)
            # 添加用户
            respository.create_user(user)
        except Exception as e:
            raise e
            

    def get_user_info(self, **conditions) -> UserDTO:
        """
        获取用户信息
        :param user_id: 用户ID
        :return: 用户信息
        """
        try:
            respository = UserRepository()
            user = respository.get_user_by_conditions(**conditions)
            return user
        except Exception as e:
            raise e

    def get_user_list(self, page: int, size: int) -> List[UserDTO]:
        """
        获取用户列表
        :return: 用户列表
        """
        try:
            respository = UserRepository()
            users = respository.get_user_list(page, size)
            return users
        except Exception as e:
            raise e