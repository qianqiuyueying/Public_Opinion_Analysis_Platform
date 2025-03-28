from sqlalchemy import Column, Integer, String, DateTime, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base
from db import Base
from datetime import datetime
from enum import Enum as PyEnum

class Type(PyEnum):
    """
    爬虫类型
    """
    APISPIDER = 'APISpider'
    PAGESIPDER = 'PageSpider'

class Spider(Base):
    __tablename__ = 'spider'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    user_id = Column(Integer, nullable=False, comment='用户ID')
    name = Column(String(255), nullable=False, comment='爬虫名称')
    description = Column(String(1000), comment='爬虫描述')
    type = Column(Enum(Type), nullable=False, comment='爬虫类型')
    request = Column(JSON, nullable=False, comment='爬虫请求参数')
    rules = Column(JSON, nullable=False, comment='爬虫解析规则')
    created_at = Column(DateTime, nullable=False, default=datetime.now, comment='创建时间')
    update_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    def __repr__(self):
        return f"<SpiderInfo(name='{self.name}', type='{self.type}')>"
    
class KeySpider(Base):
    __tablename__ = 'key_spider'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    user_id = Column(Integer, nullable=False, comment='用户ID')
    type = Column(Enum(Type), nullable=False, comment='爬虫类型')
    key = Column(String(255), nullable=False, comment='爬取关键字')
    config = Column(JSON, nullable=False, comment='爬虫配置')
    limit = Column(Integer, nullable=False, comment='爬取数量')
    created_at = Column(DateTime, nullable=False, default=datetime.now, comment='创建时间')
    update_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    request = Column()
