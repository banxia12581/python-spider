# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZhongzhiCrawlSpider(CrawlSpider):
    name = 'zhongzhi_crawl'
    allowed_domains = ['zhongzhi.com.cn']
    start_urls = ['http://www.zhongzhi.com.cn']

    rules = (
        Rule(LinkExtractor(allow=r'qyxw+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        html = response.body
        print html,response.url

