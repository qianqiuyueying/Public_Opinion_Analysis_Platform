from .model.dto import *
from .scrapyRespository import *
from util.tool import *
from rdb import *
from typing import List
from fastapi import HTTPException
from util.spider import Client

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

    def create_spider(self, spider: SpiderDTO) -> None:
        """
        创建爬虫
        :param spider: 爬虫信息
        """
        try:
            respository = scrapyRepository()
            respository.create_spider(spider)
        except Exception as e:
            raise e
        
    def delete_spider(self, spider_id: int) -> None:
        """
        删除爬虫
        :param spider_id: 爬虫id
        """
        try:    
            respository = scrapyRepository()
            respository.delete_spider(spider_id)
        except Exception as e:
            raise e
        
    def update_spider(self, spider: SpiderDTO) -> None:
        """
        更新爬虫
        :param spider: 爬虫信息
        """
        try:    
            respository = scrapyRepository()
            respository.update_spider(spider)
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
        
    def get_preview_data(self, spider: SpiderDTO):
        """
        获取爬虫预览数据
        :param spider: 爬虫信息
        """
        try:    
            print(spider)
            client = Client(address=spider.address, type=spider.type, request=spider.request)
            return client.run()
        except Exception as e:    
            raise e
    