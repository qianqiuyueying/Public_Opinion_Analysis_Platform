from fastapi import APIRouter, Body, Depends, HTTPException, Query, Path
from ..model.dto import *
from sqlalchemy.orm import Session
from ..service.userService import userService
from util.tool import create_access_token


user_router = APIRouter(prefix="/user")


@user_router.post("/login")
async def login(
    user: UserDTO = Body(...), 
    service: userService = Depends(userService)
):
    """
    登录接口
    """
    try:
        user_data = service.login(user)
        token = create_access_token({"username": user_data.username, 'user_id': user_data.id, 'role': user_data.role})
        return {"code": 200, "msg": "登录成功", "data": {"token": token}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.post("/register")
async def register(
    user: UserDTO = Body(...), 
    service: userService = Depends(userService)
):
    """
    注册接口
    """
    try:
        service.register(user)
        return {"code": 200, "msg": "注册成功"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@user_router.post("/send-verify-code")
async def send_verify_code(
    email: str = Body(...),
    username: str = Body(...),
    service: userService = Depends(userService)
):
    """
    发送验证码
    """
    try:
        service.send_verify_code1(username, email)
        return {"code": 200, "msg": "发送成功"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/info")
async def info(
    user_id: Optional[int] = Query(None),
    username: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    service: userService = Depends(userService),
):
    """
    获取用户信息
    """
    try:
        conditions = {}
        if user_id:
            conditions['id'] = user_id
        if username:
            conditions['username'] = username
        if email:
            conditions['email'] = email
        data = service.get_user_info(**conditions)
        return {"code": 200, "msg": "查询成功", "data": data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/list")
async def user_list(
    page: int = Query(1, gt=0),
    size: int = Query(10, gt=0),
    service: userService = Depends(userService),
):
    """
    获取用户列表
    """
    try:
        data = service.get_user_list(page, size)
        return {"code": 200, "msg": "查询成功", "data": data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

