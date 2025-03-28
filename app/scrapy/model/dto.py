from pydantic import BaseModel, ConfigDict
from typing import Optional


class Request(BaseModel):
    """
    请求数据传输对象
    """
    method: str
    headers: Optional[list] = None
    params: Optional[list] = None
    body: Optional[list] = None

class SpiderDTO(BaseModel):
    """
    爬虫数据传输对象
    """
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str]
    type: str
    request: Request
    rules: list[dict]

class KeySpiderDTO(BaseModel):
    """
    关键词爬虫数据传输对象
    """
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: str = None
    config: dict
    limit: str | int
    