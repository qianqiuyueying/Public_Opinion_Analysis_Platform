from .model.dto import *
from .scrapyRespository import *
from util.tool import *
from rdb import *
from typing import List
from fastapi import HTTPException
from util.spider import Client, KeyClient

class scrapyService:
    """
    爬虫模块的服务层
    """
    def get_spider(self, **conditions) -> SpiderDTO:
        """
        根据条件查询爬虫
        :param conditions: 查询条件
        :return: 爬虫信息
        """
        try:
            respository = scrapyRepository()
            spider = respository.get_spider_by_conditions(**conditions)
            return spider
        except Exception as e:
            raise e

    def create_spider(self, spider: SpiderDTO):
        """
        创建爬虫
        :param spider: 爬虫信息
        """
        try:
            respository = scrapyRepository()
            return respository.create_spider(spider)
        except Exception as e:
            raise e
        
    def delete_spider(self, spider_id: int):
        """
        删除爬虫
        :param spider_id: 爬虫id
        """
        try:    
            respository = scrapyRepository()
            return respository.delete_spider(spider_id)
        except Exception as e:
            raise e
        
    def update_spider(self, spider: SpiderDTO):
        """
        更新爬虫
        :param spider: 爬虫信息
        """
        try:    
            respository = scrapyRepository()
            return respository.update_spider(spider)
        except Exception as e:
            raise e
        
    def get_spider_list(self, user_id: int, page: int = 1, page_size: int = 10):
        """
        查询指定用户的爬虫列表
        :param user_id: 用户id
        :param page: 页码
        :param page_size: 页大小
        :return: 爬虫列表分页信息
        """
        try:
            respository = scrapyRepository()
            return respository.get_spider_list(user_id, page, page_size)
        except Exception as e:
            raise e
        

    def get_key_spider(self, **conditions) -> KeySpiderDTO:
        """
        根据条件查询关键词爬虫
        :param conditions: 查询条件
        :return: 关键词爬虫信息
        """
        try:
            respository = scrapyRepository()
            key_spider = respository.get_key_spider_by_conditions(**conditions)
            return key_spider
        except Exception as e:
            raise e
        
    def create_key_spider(self, key_spider: KeySpiderDTO):
        """
        创建关键词爬虫
        :param key_spider: 关键词爬虫信息
        """
        try:
            respository = scrapyRepository()
            return respository.create_key_spider(key_spider)
        except Exception as e:
            raise e
        
    def delete_key_spider(self, key_spider_id: int) -> None:
        """
        删除关键词爬虫
        :param key_spider_id: 关键词爬虫id
        """
        try:    
            respository = scrapyRepository()
            return respository.delete_key_spider(key_spider_id)
        except Exception as e:
            raise e
        
    
    def update_key_spider(self, key_spider: KeySpiderDTO) -> None:
        """
        更新关键词爬虫
        :param key_spider: 关键词爬虫信息
        """
        try:    
            respository = scrapyRepository()
            respository.update_key_spider(key_spider)
        except Exception as e:
            raise e
        
    
        
    def get_preview_data(self, spider: SpiderDTO):
        """
        获取爬虫预览数据
        :param spider: 爬虫信息
        """
        try:
            request = spider.request.model_dump()
            client = Client(address=spider.address, type=spider.type, request=request, rules=spider.rules)
            res = client.run()
            return res
        except Exception as e:    
            raise e
        
    def get_key_spider_preview_data(self, key_spider: KeySpiderDTO):
        """
        获取关键词类型爬虫的预览数据
        :param key_spider: 关键词爬虫信息
        """
        try:
            client = KeyClient(type=key_spider.type, config=key_spider.config, limit=key_spider.limit)
            res = client.run()
            return res
        except Exception as e:    
            raise e