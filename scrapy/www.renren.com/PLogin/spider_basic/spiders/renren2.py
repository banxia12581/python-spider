# -*- coding: utf-8 -*-
import scrapy


class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/']

    def start_requests(self):
        login_url = 'http://www.renren.com/PLogin.do'
        # 发送post请求
        data ={
            "email" : '账户',
            "password" : '密码',
        }
        yield scrapy.FormRequest(url=login_url,callback=self.after_login,formdata=data)

    #登陆以后处理
    def after_login(self, response):
        print response.body

