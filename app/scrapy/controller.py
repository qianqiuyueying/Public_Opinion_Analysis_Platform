from fastapi import APIRouter, Body, Depends, HTTPException, Query, Path, Request, Header
from .model.dto import *
from .service import *
from util.tool import *


scrapy_router = APIRouter(prefix="/scrapy")


@scrapy_router.post("/test")
async def test(header: str = Header(None)):
    print(header)
    return {"code": 200, "msg": "测试成功"}