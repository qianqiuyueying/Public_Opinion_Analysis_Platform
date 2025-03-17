from .baseSpider import APISpider, PageSpider

class Client:
    """
    客户端类
    """
    def __init__(self, address: str, type: str, request: dict, rules: list):
        self.rules = rules
        if type == 'APIClass':
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
        elif type == 'PageClass':
            params = {}
            headers = {}
            for param in request['params']:
                params.update(**param)
            for header in request['headers']:
                headers.update(**header)
            self.spider = PageSpider(address, params, headers)
        
    
    def run(self):
        return self.spider.run(self.rules)
        