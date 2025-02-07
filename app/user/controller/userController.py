from fastapi import APIRouter, Body, Depends, HTTPException, Query, Path
from ..model.dto import *
from sqlalchemy.orm import Session
from ..service.userService import userService



user_router = APIRouter(prefix="/user")


@user_router.post("/login")
def login(user: UserDTO = Body(...), service: userService = Depends(userService)):
    """
    登录接口
    """
    # return {"code": 200, "msg": "登录成功", "data": user}
    try:
        user_data = service.login(user)
        return {"code": 200, "msg": "登录成功", "data": user_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.post("/register")
def register():
    """
    注册接口
    """
    ...

@user_router.get("/info")
def info():
    """
    获取用户信息
    """
    ...

@user_router.get("/list")
def user_list():
    """
    获取用户列表
    """
    ...

@user_router.get("/logout")
def logout():
    """
    退出登录
    """
    ...