from pydantic import BaseModel, ConfigDict
from typing import Optional

class Address(BaseModel):
    """
    网址数据传输对象
    """
    type: str
    links: Optional[str]
    rule: Optional[dict]

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
    name: str
    description: Optional[str] = None
    type: str
    addr: Address
    request: Request
    rules: Optional[list] = None
    