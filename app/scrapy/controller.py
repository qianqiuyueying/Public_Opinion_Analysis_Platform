from fastapi import APIRouter, Body, Depends, HTTPException, Query, Path, Request, Header
from .model.dto import *
from .service import *
from util.tool import *


scrapy_router = APIRouter(prefix="/scrapy")

@scrapy_router.post("/get-spider")
async def get_spider(
    current_user = Depends(get_current_user), 
    spiderInfo: SpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    根据条件获取爬虫
    """
    try:
        conditions = spiderInfo.model_dump()
        conditions.push('user_id', current_user.id)
        data = service.get_spider(**conditions)
        return {'code': 200, "msg": "获取成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@scrapy_router.post("/create-spider")
async def create_spider(
    current_user = Depends(get_current_user), 
    spiderInfo: SpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    创建爬虫
    """
    try:
        spiderInfo.user_id = current_user.id
        data = service.create_spider(spiderInfo)
        return {'code': 200, "msg": "测试成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@scrapy_router.post('/delete_spider')
async def delete_spider(
    spiderInfo: SpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    删除指定爬虫
    """
    try:
        spider_id = spiderInfo.id
        data = service.delete_spider(spider_id)
        return {'code': 200, "msg": "删除成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@scrapy_router.post("/update-spider")
async def update_spider(
    spiderInfo: SpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    更新爬虫
    """
    try:
        data = service.update_spider(spiderInfo)
        return {'code': 200, "msg": "更新成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@scrapy_router.get('/get-spider-list')
async def get_spider_list(
    current_user = Depends(get_current_user), 
    page: int = Query(1, gt=0),
    size: int = Query(10, gt=0),
    service = Depends(scrapyService)
):
    """
    获取爬虫列表
    """
    try:
        data = service.get_spider_list(current_user.id, page, size)
        return {'code': 200, "msg": "获取成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@scrapy_router.post("/get-key-spider")
async def get_key_spider(
    current_user = Depends(get_current_user), 
    key_spiderInfo: KeySpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    根据条件获取关键词爬虫
    """
    try:
        conditions = key_spiderInfo.model_dump()
        conditions.push('user_id', current_user.id)
        data = service.get_key_spider(**conditions)
        return {'code': 200, "msg": "获取成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@scrapy_router.post("/create-key-spider")
async def create_key_spider(
    current_user = Depends(get_current_user), 
    key_spiderInfo: KeySpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    创建关键词爬虫
    """
    try:
        key_spiderInfo.user_id = current_user.id
        data = service.create_key_spider(key_spiderInfo)
        return {'code': 200, "msg": "创建成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@scrapy_router.post('/delete-key-spider')
async def delete_key_spider(
    key_spiderInfo: KeySpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    删除指定关键词爬虫
    """
    try:
        key_spider_id = key_spiderInfo.id
        data = service.delete_key_spider(key_spider_id)
        return {'code': 200, "msg": "删除成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@scrapy_router.post("/update-key-spider")
async def update_key_spider(
    key_spiderInfo: KeySpiderDTO = Body(...),
    service = Depends(scrapyService)
):
    """
    更新关键词爬虫
    """
    try:
        data = service.update_key_spider(key_spiderInfo)
        return {'code': 200, "msg": "更新成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@scrapy_router.post("/get-preview-data")
async def preview_data(
    spiderInfo: SpiderDTO = Body(...),
    service = Depends(scrapyService)):
    """
    获取个性化爬虫的预览数据
    """
    try:
        data = service.get_preview_data(spiderInfo)
        return {'code': 200, "msg": "获取成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@scrapy_router.post("/get-key-spider-preview-data")
async def key_spider_preview_data(
    spiderInfo: KeySpiderDTO = Body(...),
    service = Depends(scrapyService)):
    """
    获取关键词爬虫的预览数据
    """
    try:
        data = service.get_key_spider_preview_data(spiderInfo)
        return {'code': 200, "msg": "获取成功", 'data': data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
