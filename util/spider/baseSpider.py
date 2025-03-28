from DrissionPage import Chromium, ChromiumOptions, SessionPage
from abc import ABC, abstractmethod
from DrissionPage._elements.chromium_element import ChromiumElement
from typing import Union
from random import randint
import numpy as np
import re
from pprint import pprint
import queue
from util.tool import get_time
from DrissionPage.common import Keys

class APISpider:
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
        self.session = SessionPage()
        if method == "GET":
            self.session.get(url=address, params=params, headers=headers)
        elif method == 'POST':
            self.session.post(url=address, params=params, headers=headers, json=json)

    def run(self, rules: list):
        """
        执行爬虫方法
        :param rules: 规则列表
        """
        # 原始数据
        data = [self.session.response.json()]
        if not rules:
            return data
        res = []
        for rule in rules:
            source = rule.get('source')
            operate = rule.get('operate')
            source_data = self.select(data, source)
            tem = self.select(source_data, operate)
            res.append(tem)
        self.session.close()
        return res
    
    def select(self, raw_data, locators: list) -> list:
        """
        根据 locators 规则列表选择元素
        """
        if locators[0] == 'root' or len(locators) == 0:
            return raw_data
        for locator in locators:
            # 临时变量
            tem = []
            if locator.startswith('.'):
                for i in raw_data:
                    tem.append(i.get(locator[1:]))
            elif locator.startswith('['):
                indexes = locator[1:-1].split(',')
                for i in raw_data:
                    for index in indexes:
                        tem.append(i[int(index)])
            raw_data = tem
        return raw_data
            


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
        co = ChromiumOptions().headless(headless).auto_port()
        self.tab = Chromium(co).latest_tab
        self.tab.get(address)


    def run(self, rules: list):
        """
        执行爬虫方法
        :param rules: 规则列表
        """
        # 原始数据存一份
        raw_ele = self.tab
        if not rules:
            return [raw_ele.text]
        res = []
        for rule in rules:
            source = rule.get('source')
            operate = rule.get('operate')
            tem = self.helper(source, operate)
            res.append(tem)
        return res


    def helper(self, source, operate) -> list:
        """
        辅助函数，对源进行对应的操作
        """
        if operate[0] == 'click': # 点击
            ele = self.select(source)
            ele.click()
            return True
        elif operate[0] == 'listen':  # 监听
            self.tab.listen.start(source[0])
            packet = self.tab.listen.wait()
            return packet.response.body
        elif operate[0] == 'scroll':  # 滚动
            ele = self.select(source)
            ele.scroll(100)
            return True
        else:   # 元素选择
            _ = self.select(source, self.tab)
            return self.select(operate, _)
    def select(self, rules: list, element=None):
        """
        选取函数，选中指定的元素并返回
        """
        if rules[0] == 'root' or len(rules) == 0:
            return self.tab
        if len(rules) > 1:
            for rule in rules[:-2]:
                element = element.ele(rule)
            return element.ele(rules[-1]).text
        else:
            return element.ele(rules[0]).text


class RedNoteSpider:
    """
    小红书爬虫
    """
    def __init__(self, config: dict, limit: int = 10, headless=False):
        """
        初始化
        :param config: 配置信息
        :param limit: 爬取数量
        """
        key = config.get('key')
        self.limit = limit  # 开发临时配置，需转为limit
        co = ChromiumOptions().headless(headless).set_local_port(30111)
        self.tab = Chromium(co).latest_tab
        url = f'https://www.xiaohongshu.com/search_result?keyword={key}&source=web_explore_feed'
        # 开始设置监听
        self.tab.listen.start('https://edith.xiaohongshu.com/api/sns/web/v1/search/notes')
        self.tab.get(url)
        # 选择note类型
        NoteType = config.get('NoteType')
        if NoteType == 'all':
            ele = self.tab.ele('#note')
            ele.click()
        elif NoteType == 'article':
            ele = self.tab.ele('#short_note')
            ele.click()
        elif NoteType == 'video':
            ele = self.tab.ele('#video_note')
            ele.click()
        # 选择note排序方式
        filter_ele = self.tab.ele('.filter')
        filter_ele.click()
        sortedBy = config.get('sortedBy')
        if sortedBy == 'general':
            ele = self.tab.ele('tag=span@text()= 综合 ')
            ele.click()
        elif sortedBy == 'new':
            ele = self.tab.ele('tag=span@text()= 最新 ')
            ele.click()
        elif sortedBy == 'hot':
            ele = self.tab.ele('tag=span@text()= 最热 ')
            ele.click()
        
    
    def scrapy(self) -> list:
        """
        抓取方法
        """
        # 记录当前爬取数量，记录爬取到的评论 浏览 -> 笔记 -> 评论
        data = []
        # 只要未达限制就继续循环
        while len(data) < int(self.limit):
            # 获取一个浏览数据包
            packet = self.tab.listen.wait()
            notes = packet.response.body['data']['items']
            # 遍历取出来数据包中的笔记
            for note in notes:
                # 提取出爬取笔记链接中评论必要的信息
                note_id = note.get('id')
                xsec_token = note.get('xsec_token')
                self.get_note_info(self.limit, data, note_id, xsec_token)
                if len(data) >= int(self.limit):
                    break
        return data


    
    def get_note_info(self, limit: int, data: list, note_id, xsec_token, cursor=""):
        """
        具体抓取每个note的文章以及评论信息
        :param limit: 抓取的数量
        :param data: 抓取的数据
        :param note_id: note的id
        :param xsec_token: xsec_token
        :param cursor: 评论的游标，用于获取所有的评论
        """
        url = f'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id={note_id}&cursor={cursor}&top_comment_id=&image_formats=jpg,webp,avif&xsec_token={xsec_token}'
        # 先切到session模式 获取note相关的信息
        self.tab.change_mode('s')
        self.tab.get(url)
        self.tab.wait(2, 5)
        response = self.tab.response.json()
        for comment in response.get('data').get('comments'):
            if len(data) >= int(limit):
                break
            user_name = comment.get('user_info').get('nickname')
            content = comment.get('content')
            create_time = get_time(comment.get('create_time'))
            like_count = comment.get('like_count')
            data.append({"user_name": user_name, 'content': content, 'create_time': create_time, 'like_count': like_count})
            if len(data) >= int(limit):
                break
            subcomments = comment.get('sub_comments')
            for subcomment in subcomments:
                user_name = subcomment.get('user_info').get('nickname')
                content = subcomment.get('content')
                create_time = get_time(subcomment.get('create_time'))
                like_count = subcomment.get('like_count')
                data.append({"user_name": user_name, 'content': content, 'create_time':create_time, 'like_count': like_count})
                if len(data) >= int(limit):
                    break
        if response.get('data').get('has_more'):
            cursor = response.get('data').get('cursor')
            self.get_note_info(limit, data, note_id, xsec_token, cursor)
        # 最后切回driver 模式
        self.tab.change_mode('d')
        
                

class WeiboSpider:
    """
    微博爬虫
    """
    def __init__(self, config: dict, limit: int = 10, headless=False):
        """
        初始化
        :param config: 配置信息
        :param limit: 爬取数量
        """
        key = config['key']
        self.limit = limit
        co = ChromiumOptions().headless(headless).set_local_port(30222)
        self.chromium = Chromium(co)
        self.tab = self.chromium.latest_tab
        url = ""
        blogType = config.get('blogType')
        if blogType == 'all':
            url = f"https://s.weibo.com/weibo?q={key}&typeall=1&suball=1"
        elif blogType == 'hot':
            url = f"https://s.weibo.com/weibo?q={key}&xsort=hot&suball=1"
        elif blogType == 'original':
            url = f"https://s.weibo.com/weibo?q={key}&scope=ori&suball=1"
        elif blogType == 'vip':
            url = f"https://s.weibo.com/weibo?q={key}&vip=1&suball=1"
        elif blogType == 'media':
            url = f"https://s.weibo.com/weibo?q={key}&category=4&suball=1"
        elif blogType == 'view':
            url = f"https://s.weibo.com/weibo?q={key}&viewpoint=1&suball=1"
        if config.get('time'):
            url += config.get('time')
        url += 'Refer=g&page=0'
        self.url = url

    def scrapy(self):
        data = []
        # 获得浏览页面的item
        index = 1
        while len(data) < int(self.limit):
            self.url = self.url.replace(f'page={index-1}', f'page={index}')
            print(self.url)
            self.tab.get(self.url)
            index += 1
            items = self.tab.s_eles('.card-wrap')
            for item in items:
                if len(data) >= int(self.limit):
                    break
                user_name = item.ele('tag=a@class=name').text
                content = item.ele('tag=p@class=txt').text
                create_time = item.ele('.from').ele('tag=a').text
                like_count = item.ele('tag=a@title=赞').text
                data.append({"user_name": user_name, 'content': content, 'create_time': create_time, 'like_count': like_count})
                if len(data) >= int(self.limit):
                    break
                link = item.ele('.from').ele('tag=a').link
                # 获取每个页面的link并访问获取信息
                self.get_blog_info(data, link)
        return data
    
    def get_blog_info(self, data, link):
        new_tab = self.chromium.new_tab()
        # 设置监听
        new_tab.listen.start('https://weibo.com/ajax/statuses/buildComments')
        new_tab.get(link)
        for packet in new_tab.listen.steps(timeout=2):
            # 每次接收到新的数据包都滚动到底部
            new_tab.scroll.to_bottom()
            if len(data) >= int(self.limit) or packet.response.body.get('max_id') == '0' or len(packet.response.body.get('data')) == 0:
                new_tab.listen.stop()
                break
            items = packet.response.body.get('data')
            for item in items:
                if len(data) >= int(self.limit):
                    new_tab.listen.stop()
                    break
                user_name = item.get('user').get('screen_name')
                content = item.get('text_raw')
                create_time = item.get('create_at')
                like_count = item.get('like_counts')
                data.append({"user_name": user_name, 'content': content, 'create_time': create_time, 'like_count': like_count})
                if item.get('comments'):
                    for comment in item.get('comments'):
                        if len(data) >= int(self.limit):
                            new_tab.listen.stop()
                            break
                        user_name = comment.get('user').get('screen_name')
                        content = comment.get('text')
                        create_time = comment.get('created_at')
                        like_count = comment.get('like_counts')
                        data.append({"user_name": user_name, 'content': content, 'create_time': create_time, 'like_count': like_count})
        new_tab.close()


        
        

class TiktokSpider:
    """
    抖音爬虫
    """
    def __init__(self, config: dict, limit: int = 10, headless=False):
        """
        初始化
        :param config: 配置信息
        :param limit: 爬取数量
        """
        key = config['key']
        self.limit = limit
        co = ChromiumOptions().headless(headless).set_local_port(30333)
        self.chromium = Chromium(co)
        self.tab = self.chromium.latest_tab
        self.tab.get(f'https://www.douyin.com/root/search/{key}')
        # 点击筛选按钮
        sort_ele = self.tab.ele('text=筛选')
        if sort_ele:
            self.tab.wait(2)
            sort_ele.click()
            sort_ele.click()

        # 设置排序依据
        sortedBy = config.get('sortedBy')
        if sortedBy == 'general':
            general_ele = self.tab.ele('tag=span@@data-index1=0@@data-index2=0')
            general_ele.click(by_js=True)
        elif sortedBy == 'new':
            new_ele = self.tab.ele('tag=span@@data-index1=0@@data-index2=1')
            new_ele.click(by_js=True)
        elif sortedBy == 'hot':
            hot_ele = self.tab.ele('tag=span@@data-index1=0@@data-index2=2')
            hot_ele.click(by_js=True)
        # 设置发布时间
        publish_time = config.get('publishTime')
        if publish_time == 'all':
            all_ele = self.tab.ele('tag=span@@data-index1=1@@data-index2=0')
            all_ele.click(by_js=True)
        elif publish_time == 'day':
            day_ele = self.tab.ele('tag=span@@data-index1=1@@data-index2=1')
            day_ele.click(by_js=True)
        elif publish_time == 'week':
            week_ele = self.tab.ele('tag=span@@data-index1=1@@data-index2=2')
            week_ele.click(by_js=True)
        elif publish_time == '6months':
            months_ele = self.tab.ele('tag=span@@data-index1=1@@data-index2=3')
            months_ele.click(by_js=True)
        # 设置视频时长
        duration = config.get('duration')
        if duration == 'all':
            all_ele = self.tab.ele('tag=span@@data-index1=2@@data-index2=0')
            all_ele.click(by_js=True)
        elif duration == 'lessThan1Minute':
            lessThan1Minute_ele = self.tab.ele('tag=span@@data-index1=2@@data-index2=1')
            lessThan1Minute_ele.click(by_js=True)
        elif duration == '1To5Minute':
            to5Minute_ele = self.tab.ele('tag=span@@data-index1=2@@data-index2=2')
            to5Minute_ele.click(by_js=True)
        elif duration == 'moreThan5Minute':
            moreThan5Minute_ele = self.tab.ele('tag=span@@data-index1=2@@data-index2=3')
            moreThan5Minute_ele.click(by_js=True)
        # 设置内容形式
        contentType = config.get('contentType')
        if contentType == 'all':
            all_ele = self.tab.ele('tag=span@@data-index1=4@@data-index2=0')
            all_ele.click(by_js=True)
        elif contentType == 'article':
            article_ele = self.tab.ele('tag=span@@data-index1=4@@data-index2=1')
            article_ele.click(by_js=True)
        elif contentType == 'video':
            video_ele = self.tab.ele('tag=span@@data-index1=4@@data-index2=2')
            video_ele.click(by_js=True)

    def scrapy(self):
        data = []
        ele = self.tab.eles('#^waterfall_item')[0]
        # 跳转至视频滚动页面
        ele.click()
        self.tab.listen.start('https://www.douyin.com/aweme/v1/web/comment/list/')
        comment_ele = self.tab.ele('@data-e2e=feed-comment-icon')
        comment_ele.click()
        while len(data) < int(self.limit):
            for packet in self.tab.listen.steps(timeout=3):
                if len(data) >= int(self.limit):
                        break
                comments = packet.response.body.get('comments')
                scroll_ele = self.tab.ele('@data-e2e=comment-list')
                scroll_ele.scroll.to_bottom()
                if not comments:
                    break
                for comment in comments:
                    if len(data) >= int(self.limit) or packet.response.body.get('has_more') == '0':
                        break
                    user_name = comment.get('user').get('nickname')
                    content = comment.get('text')
                    create_time = get_time(comment.get('create_time'))
                    like_count = comment.get('digg_count')
                    data.append({"user_name": user_name, 'content': content, 'create_time': create_time, 'like_count': like_count})
            scroll_page_ele = self.tab.ele('tag=xg-video-container')
            scroll_page_ele.input(Keys.DOWN)
        return data