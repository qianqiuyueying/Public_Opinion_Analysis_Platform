from fastapi import APIRouter, Depends, HTTPException, Body, Request
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler

from ..user.userServiceImpl import *
from ..user.pojo.userDTO import *

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get('/')
async def test():
    print("test")
    return JSONResponse({"message": "Hello World"})

@user_router.post("/login")
async def login(user: UserDTO = Body(...), user_service: UserServiceImpl = Depends(UserServiceImpl)):
    print(user)
    # data = user_service.get_user_info(user)
    return JSONResponse(content={
        "message": "Hello World",
    }, status_code=200)


