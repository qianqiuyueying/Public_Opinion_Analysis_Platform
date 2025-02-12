from fastapi import FastAPI, Request, HTTPException
from config import *
import jwt
from db import init_db
from .user.controller.userController import user_router
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
        
        white_list = [
            "/user/login",
            "/user/register",
            "/user/send_verify_code",
            '/user/info',
            "/user/list"
        ]
        
        # 精确匹配路径
        if request.url.path in white_list:
            response = await call_next(request)
            return response
        
        authorization: str = request.headers.get("Authorization")
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid token")
        
        token = authorization[7:]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            request.state.user = payload
        except jwt.PyJWTError as e:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        # 继续处理请求并添加处理时间头
        response = await call_next(request)
        return response
    
    app.include_router(user_router)
    
    return app
