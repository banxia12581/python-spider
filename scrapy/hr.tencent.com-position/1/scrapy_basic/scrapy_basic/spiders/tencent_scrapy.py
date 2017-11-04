# -*- coding: utf-8 -*-
import scrapy
from scrapy_basic.items import PositionItem

class TencentScrapySpider(scrapy.Spider):
    name = 'tencent_scrapy'
    allowed_domains = ['hr.tencent.com']
    page = 0
    # 爬虫起始URL
    base_urls = 'http://hr.tencent.com/position.php?start=%d'
    start_urls = [ base_urls % page]



    def parse(self, response):
        #匹配所有的职位tr
        position_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for position in position_list:
            item = PositionItem()
            item['position_name'] = position.xpath('.//td[1]//a/text()').extract()[0]
            fa = lambda x:x[0] if x else ''
            item['position_link'] = fa(position.xpath('.//td[1]//a/@href').extract())
            item['position_type'] = fa(position.xpath('.//td[2]/text()').extract())
            item['position_num'] = fa(position.xpath('.//td[3]/text()').extract())
            item['location'] = fa(position.xpath('.//td[4]/text()').extract())
            item['date_pub'] = fa(position.xpath('.//td[5]/text()').extract())

            yield item

        if self.page < 500:
            self.page += 10
            # 构造请求，生成请求，加入队列
            yield scrapy.Request(self.base_urls % self.page,callback=self.parse)




