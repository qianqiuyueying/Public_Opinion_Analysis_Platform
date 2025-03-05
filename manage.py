from fastapi import FastAPI, HTTPException
from fastapi import Request
import jwt
import uvicorn
from app import init_app
from db import init_db
from config import *

app = init_app()

@app.get("/test")
async def test(request: Request):
    print(request.headers)
    return {"code": 200, "msg": "测试成功"}


if __name__ == '__main__':
    # app = init_app()
    uvicorn.run('manage:app', host='127.0.0.1', port=8000, reload=True)