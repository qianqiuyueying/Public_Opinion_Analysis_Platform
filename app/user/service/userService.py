from ..model.dto import *
from ..repository.userRespository import *
from fastapi import Depends, HTTPException
from util.tool import *

class userService:
    """
    用户模块的服务层
    """
    def login(self,
                user: UserDTO,
                respository: UserRepository = Depends(),
                password_manager: PasswordManager = Depends()) -> UserDTO:
        """
        用户登录
        :param user: 用户信息
        :return: 用户信息
        """
        try:
            user_data = respository.get_user_by_username(user.username)
            if user_data is None:
                raise HTTPException(status_code=404, detail="用户不存在")
            if password_manager.check_password(user.password, user_data.password):
                raise HTTPException(status_code=400, detail="密码错误")
            respository.set_login(user_data.id)
            return user_data
        except Exception as e:
            raise e
            
