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
        driver = SessionPage()
        if method == "get":
            self.data = driver.get(address, params=params, headers=headers)
        elif method == 'post':
            self.data = driver.post(address, params=params, headers=headers, json=json)

    def run(self, rules: dict):
        res = None
        for (source, operate) in rules.items():
            if source == 'root':
                res = self.data.json
        return res


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

    def get(self) -> None: 
        """
        初始化浏览器并打开指定页面等待后续步骤
        """
        self.driver.get(self.address, params=self.params, headers=self.headers)

    def select(self, value: str):
        """
        根据规则选取页面中元素
        :param value: 规则
        """
        ...

    def action(self, value: str) -> None:
        """
        对选取的元素进行指定动作
        :param value: 指定动作
        """
        ...
    
    def listen(self, value: str) -> None:
        """
        监听页面接口
        :param value: 接口特征
        """
        ...

    def close(self):
        """
        关闭浏览器释放资源
        """
        self.driver.quit()

    
