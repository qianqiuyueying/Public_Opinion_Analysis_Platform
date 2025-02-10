from ..model.dto import *
from ..repository.userRespository import *
from fastapi import HTTPException
from util.tool import *

class userService:
    """
    用户模块的服务层
    """
    def login(self, user: UserDTO):
        """
        用户登录
        :param user: 用户信息
        :return: 用户信息
        """
        try:
            respository = UserRepository()
            user_data = respository.get_user_by_username(user.username)  # 数据库用户信息
            if user_data is None:
                raise HTTPException(status_code=404, detail="用户不存在")
            password_manager = PasswordManager()
            if password_manager.check_password(user_data.password, user.password):
                raise HTTPException(status_code=400, detail="密码错误")
            respository.set_login(user_data.id)
            return user_data
        except Exception as e:
            raise e
            
