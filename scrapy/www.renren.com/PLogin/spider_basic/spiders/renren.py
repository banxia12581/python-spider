# -*- coding: utf-8 -*-
import scrapy

#模拟登录
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/']
    headers={
        'Host' : 'www.renren.com',
        'Connection' : 'keep-alive',
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.8',
    }
    cookies = {
        '登录之后的cookies'
    }
    #重写第一次请求的处理函数,返回requests对象
    def start_requests(self):
        start_url = 'http://www.renren.com/365577233'
        yield scrapy.Request(url=start_url,headers=self.headers,callback=self.parse,cookies=self.cookies)

    def parse(self, response):
        print response.body
