from .baseSpider import APISpider, PageSpider

class Client:
    """
    客户端类
    """
    def __init__(self, address: str, type: str, request: dict, rules: list):
        self.rules = rules
        if type == 'APISPider':
            params = {}
            headers = {}
            json = {}
            for param in request['params']:
                params.update(**param)
            for header in request['headers']:
                headers.update(**header)
            for data in request['body']:
                json.update(**data)
            self.spider = APISpider(address, type, params, headers, json)
        elif type == 'PageSpider':
            params = {}
            headers = {}
            for param in request['params']:
                params.update(**param)
            for header in request['headers']:
                headers.update(**header)
            self.spider = PageSpider(address, params, headers)
        
    
    def run(self):
        self.spider.run(self.rules)
        