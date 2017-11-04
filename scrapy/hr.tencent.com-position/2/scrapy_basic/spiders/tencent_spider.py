# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

from scrapy_basic.items import TencentCrawlItem


class TencentSpiderSpider(CrawlSpider):
    name = 'tencent_spider'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php/']

    rules = (
        # follow : 是否跟进页面 根据规则 进行再次提取链接
        Rule(LinkExtractor(allow=(r'position_detail',)), callback='parse_item', follow=False,process_links='pro_link'),
        Rule(LinkExtractor(allow=(r'start=\d+',)), follow=True),
    )

    # 处理职位详情
    def parse_item(self, response):
        item = TencentCrawlItem()
        position_name = response.xpath('//tr[@class="h"]/td/text()').extract()
        position_name = self.getVal(position_name)
        location = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()
        location = self.getVal(location)
        position_type = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract()
        position_type = self.getVal(position_type)
        position_num = response.xpath('//tr[@class="c bottomline"]/td[3]/text()').extract()
        position_num = self.getVal(position_num)
        position_num = self.getNum(position_num)
        position_duty = response.xpath('//tr[@class="c"][1]//ul[@class="squareli"]//li/text()').extract()
        requestion = response.xpath('//tr[@class="c"][2]//ul[@class="squareli"]/li/text()').extract()
        position_url = response.url

        item['position_name'] = position_name
        item['location'] = location
        item['position_type'] = position_type
        item['position_num'] = position_num
        item['position_duty'] = position_duty
        item['position_url'] = position_url
        item['requestion'] = requestion

        # print position_duty,requestion,type(position_duty),type(requestion)
        # print '-'*200
        yield item


    # 处理链接
    def pro_link(self, links):
        for link in links:
            link.url = link.url.replace('position.php/','')
        return links

    def getNum(self,data):
        num_re = re.compile(r'\d+')
        res = num_re.search(data)
        if res is not None:
            return int(res.group())
        else:
            return int(0)

    def getVal(self,data):
        return data[0] if data else ''