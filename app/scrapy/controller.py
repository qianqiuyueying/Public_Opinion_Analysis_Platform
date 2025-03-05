from fastapi import APIRouter, Body, Depends, HTTPException, Query, Path, Request, Header
from .model.dto import *
from .service import *
from util.tool import *


scrapy_router = APIRouter(prefix="/scrapy")

@scrapy_router.post("/create-spider")
async def create_spider(
    current_user = Depends(get_current_user), 
    spiderInfo: SpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    创建爬虫
    """
    print(current_user)
    # print(spiderInfo)
    return {'code': 200, "msg": "测试成功"}


@scrapy_router.post("/get-preview-data")
async def preview_data(
    spiderInfo: SpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    service.get_preview_data(spiderInfo)
    return {'code': 200, "msg": "测试成功"}