from sqlalchemy import Column, Integer, String, DateTime, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base
from db import Base
from datetime import datetime
from enum import Enum as PyEnum

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键ID')
    user_id = Column(Integer, nullable=False, comment='用户ID')
    spider_list = Column(JSON, nullable=False, comment='该任务配置的爬虫列表')
    status = Column(Enum('未开始', '进行中', '已完成'), nullable=False, comment='任务状态')
    created_at = Column(DateTime, nullable=False, default=datetime.now, comment='创建时间')
    update_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')