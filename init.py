from http.server import BaseHTTPRequestHandler

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.userController import *


# before request中间件
class BeforeRequestMiddleware(BaseHTTPMiddleware):
    """
    请求中间件类，必须继承BaseHTTPMiddleware
    添加必要的身份校验
    """
    async def dispatch(self, request: Request, call_next):
        print(request.url)
        response = await call_next(request)
        return response
        


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.add_middleware(BeforeRequestMiddleware)
    @app.exception_handler(Exception)
    async def handle_exception(request: Request, exc: Exception):
        print(request.body)
        return JSONResponse({"error": str(exc)}, status_code=500)

    return app
