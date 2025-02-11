from ..model.dto import *
from ..repository.userRespository import *
from fastapi import HTTPException
from util.tool import *
from rdb import *
from random import randint

class userService:
    """
    用户模块的服务层
    """
    def login(self, user: UserDTO) -> None:
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
            respository.set_login(user_data.id)
            return user_data
        except Exception as e:
            raise e
        
    def send_verify_code(self, email: str) -> None:
        """
        发送验证码
        :param email: 邮箱地址
        """
        try:
            # 生成验证码
            code = randint(100000, 999999)
            # 发送验证码
            send_verify_code(email, code)
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
            if code != true_code:
                raise HTTPException(status_code=400, detail="验证码错误")
            # 判断用户是否存在
            respository = UserRepository()
            if respository.get_user_by_username(user.username) is not None:
                raise HTTPException(status_code=400, detail="用户已存在")
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
