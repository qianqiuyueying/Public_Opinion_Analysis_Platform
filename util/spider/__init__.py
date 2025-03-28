from .baseSpider import APISpider, PageSpider, RedNoteSpider, WeiboSpider, TiktokSpider

class Client:
    """
    个性化爬虫客户端类
    """
    def __init__(self, address: str, type: str, request: dict, rules: list):
        self.rules = rules
        if type == 'APIClass':  # api类型爬虫
            params = {}
            headers = {}
            json = {}
            for param in request['params']:
                params.update(**param)
            for header in request['headers']:
                headers.update(**header)
            for data in request['body']:
                json.update(**data)
            self.spider = APISpider(address, request['method'], params, headers, json)
        elif type == 'PageClass': # 页面类型爬虫
            params = {}
            headers = {}
            for param in request['params']:
                params.update(**param)
            for header in request['headers']:
                headers.update(**header)
            self.spider = PageSpider(address, params, headers)
    
    def run(self):
        return self.spider.run(self.rules)
    
class KeyClient:
    """
    关键词类型爬虫的客户端
    """
    def __init__(self, type: str, config: dict, limit: int):
        if type == 'RedNote':
            self.spider = RedNoteSpider(config, limit)
        elif type == 'Weibo':
            self.spider = WeiboSpider(config, limit)
        elif type == 'Tiktok':
            self.spider = TiktokSpider(config, limit)
    
    def run(self):
        return self.spider.scrapy()
        