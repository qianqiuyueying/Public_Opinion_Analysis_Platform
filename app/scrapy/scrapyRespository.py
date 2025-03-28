from .model.data_model import *
from .model.dto import *
from db import get_session
from util.tool import now
from sqlalchemy import and_
from fastapi import HTTPException

class scrapyRepository:
    def __init__(self):
        self.session = next(get_session())

    def create_spider(self, spider: SpiderDTO):
        """
        创建爬虫
        :param spider: 爬虫信息
        """
        try:
            spider_info = Spider(
                name=spider.name,
                user_id=spider.user_id,
                type=spider.type,
                description=spider.description,
                address=spider.address,
                request=spider.request,
                rules=spider.rules,
                created_at=now(),
                updated_at=now()
            )
            self.session.add(spider_info)
            self.session.commit()
            return spider_info
        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_spider_by_conditions(self, **conditions):
        """
        根据条件获取爬虫信息
        :param conditions: 查询条件
        """
        try:
            spider = self.session.query(Spider).filter_by(**conditions).first()
            return spider
        except Exception as e:
            raise e
        
    def update_spider(self, spider: SpiderDTO):
        """
        更新爬虫信息
        :param spider: 爬虫信息
        """
        try:
            spider_info = self.session.query(Spider).filter_by(id=spider.id).first()
            spider_info.name = spider.name
            spider_info.user_id = spider.user_id
            spider_info.type = spider.type
            spider_info.description = spider.description
            spider_info.address = spider.address
            spider_info.request = spider.request
            spider_info.rules= spider.rules
            spider_info.updated_at = now()
            self.session.commit()
            return spider_info
        except Exception as e:
            self.session.rollback()
            raise e
        
    def delete_spider(self, spider_id: int):
        """
        删除爬虫
        :param spider_id: 爬虫ID
        """
        try:
            rows_affected = self.session.query(Spider).filter_by(id=spider_id).delete()
            self.session.commit()
            return rows_affected > 0
        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_spider_list(self, user_id: int, page: int = 1, page_size: int = 10):
        """
        获取指定用户的爬虫列表
        :param user_id: 用户ID
        :param page: 页码
        :param page_size: 每页数量
        :return: 爬虫列表
        """
        try:
            # 添加根据用户ID过滤的条件
            spider_list = self.session.query(Spider).filter(Spider.user_id == user_id).offset((page - 1) * page_size).limit(page_size).all()
            return {
                "spider_list": spider_list,
                "total": self.session.query(Spider).filter(Spider.user_id == user_id).count(),
                "page": page,
                "page_size": page_size
            }
        except Exception as e:
            raise e
    

    def create_key_spider(self, key_spider: KeySpiderDTO):
        """
        创建关键词爬虫
        :param key_spider: 关键词爬虫信息
        """
        try:
            key_spider_info = KeySpider(
                user_id = key_spider.user_id,
                type = key_spider.type,
                key = key_spider.key,
                config = key_spider.config,
                limit = key_spider.limit,
                created_at=now(),
                updated_at=now()
            )
            self.session.add(key_spider_info)
            self.session.commit()
            return key_spider_info
        except Exception as e:
            self.session.rollback()
            raise e

    def get_key_spider_by_conditions(self, **conditions):
        """
        根据条件获取关键词爬虫信息
        :param conditions: 查询条件
        """
        try:
            key_spider = self.session.query(KeySpider).filter_by(**conditions).first()
            return key_spider
        except Exception as e:
            raise e
        

    def update_key_spider(self, key_spider: KeySpiderDTO):
        """
        更新关键词爬虫信息
        :param key_spider: 关键词爬虫信息
        """
        try:
            key_spider_info = self.session.query(KeySpider).filter_by(id=key_spider.id).first()
            key_spider_info.user_id = key_spider.user_id
            key_spider_info.type = key_spider.type
            key_spider_info.key = key_spider.key
            key_spider_info.config = key_spider.config
            key_spider_info.limit = key_spider.limit
            key_spider_info.updated_at = now()
            self.session.commit()
            return key_spider_info
        except Exception as e:
            self.session.rollback()
            raise e
        
    
    def delete_key_spider(self, key_spider_id: int):
        """
        删除关键词爬虫
        :param key_spider_id: 关键词爬虫ID
        """
        try:
            rows_affected = self.session.query(KeySpider).filter_by(id=key_spider_id).delete()
            self.session.commit()
            return rows_affected > 0
        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_key_spider_list(self, user_id: int, page: int = 1, page_size: int = 10):
        """
        获取指定用户的关键词爬虫列表
        :param user_id: 用户ID
        :param page: 页码
        :param page_size: 每页数量
        :return: 关键词爬虫列表
        """
        try:
            # 添加根据用户ID过滤的条件
            key_spider_list = self.session.query(KeySpider).filter(KeySpider.user_id == user_id).offset((page - 1) * page_size).limit(page_size).all()
            return {
                "key_spider_list": key_spider_list,
                "total": self.session.query(KeySpider).filter(KeySpider.user_id == user_id).count(),
                "page": page,
                "page_size": page_size
            }
        except Exception as e:
            raise e