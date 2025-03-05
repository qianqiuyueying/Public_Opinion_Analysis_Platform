from fastapi import FastAPI, Request, HTTPException
from config import *
import jwt
from db import init_db
from .user.controller.userController import user_router
from .scrapy.controller import scrapy_router
from fastapi.middleware.cors import CORSMiddleware


def init_app():
    init_db()
    app = FastAPI()
        # CORS中间件需最先添加以确保正确处理头部
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", 'http://localhost'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    

    
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        # 处理OPTIONS预检请求
        if request.method == "OPTIONS":
            response = await call_next(request)
            return response
        
        # 创建白名单，方便debug以及未登录用户使用
        white_list = [
            "/docs",
            "/openapi.json",
            "/user/login",
            "/user/register",
            "/user/send-verify-code",
            "/user/info",
            '/icons/icon_zh_48.png'
        ]
        
        if request.url.path in white_list:
            response = await call_next(request)
            return response
        
        # 校验用户是否登录
        authorization: str = request.headers.get("Authorization")
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid token")
        
        # 取出token后续使用
        token = authorization[7:]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            # 验证是否有权访问路径
            # 将登录用户的必要信息存进request，方便controller使用
            request.state.user = payload
        except jwt.PyJWTError as e:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        # 继续处理请求并添加处理时间头
        response = await call_next(request)
        return response
    
    app.include_router(user_router)
    app.include_router(scrapy_router)
    
    return app
