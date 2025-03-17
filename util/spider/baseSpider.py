from DrissionPage import ChromiumPage, ChromiumOptions, SessionPage
from abc import ABC, abstractmethod
from DrissionPage._elements.chromium_element import ChromiumElement
from typing import Union
from random import randint
import numpy as np
import re

class APISpider():
    """
    创建一个api爬虫
    """
    def __init__(self, address: str, method: str, params: dict, headers: dict, json: dict):
        """
        初始化
        :param address: 爬虫网址
        :param method: 请求方法
        :param params: 请求参数
        :param headers: 请求头
        :param json: 请求体
        """
        super().__init__()
        self.session = SessionPage()
        if method == "GET":
            self.session.get(address, params=params, headers=headers)
        elif method == 'POST':
            self.session.post(address, params=params, headers=headers, json=json)

    def run(self, rules: list):
        """
        执行爬虫方法
        :param rules: 规则列表
        """
        try:
            # 结果列表
            res = []
            # 遍历每一条规则
            for rule in rules:
                # 取出操作源和操作
                source = rule['source']
                operate = rule['operate']
                # 进行操作并将结果记录
                res.append(self.select(source, operate))
            return res
        except Exception as e:
            raise e
        
def select(self, source: list | str, operate: list) -> list:
    ...
    



class PageSpider():
    """
    创建一个页面爬虫
    """
    def __init__(self, address: str, params: dict, headers: dict, headless=False) -> None:
        """
        初始化
        :param address: 爬虫网址
        :param params: 请求参数
        :param headers: 请求头
        :param headless: 是否开启无头模式
        """
        super().__init__()
        co = ChromiumOptions().headless(headless)
        self.driver = ChromiumPage(co)
        self.address = address
        self.params = params
        self.headers = headers

    def run(self, rules: list):
        """
        执行爬虫方法
        :param rules: 规则列表
        """
        print(rules)
        return 0


    
