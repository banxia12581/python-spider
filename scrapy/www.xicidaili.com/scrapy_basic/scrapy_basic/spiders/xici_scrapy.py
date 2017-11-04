# -*- coding: utf-8 -*-
import scrapy
from scrapy_basic.items import ProxyItem

class XiciScrapySpider(scrapy.Spider):
    name = 'xici_scrapy'
    allowed_domains = ['www.xicidaili.com']

    page = 1
    base_url = 'http://www.xicidaili.com/nt/%d'
    start_urls = [base_url % page]

    def parse(self, response):
        proxy_list = response.xpath('//table[@id="ip_list"]//tr')[1:]
        fa = lambda x : x[0] if x else ''
        for proxy in proxy_list:
            item = ProxyItem()
            addr = proxy.xpath('./td[2]/text()').extract()
            addr = self.getVal(addr)
            port = proxy.xpath('./td[3]/text()').extract()
            port = self.getVal(port)
            location = proxy.xpath('./td[4]/a/text()').extract()
            location = self.getVal(location)
            http_type = proxy.xpath('./td[6]/text()').extract()
            http_type = self.getVal(http_type)
            speed = proxy.xpath('./td[7]/div/@title').extract()
            speed = self.getVal(speed)
            connect_speed = proxy.xpath('./td[8]/div/@title').extract()
            connect_speed = self.getVal(connect_speed)
            alive_time = proxy.xpath('./td[9]/text()').extract()
            alive_time = self.getVal(alive_time)

            item['addr'] = addr
            item['port'] = port
            item['location'] = location
            item['http_type'] = http_type
            item['speed'] = speed
            item['connect_speed'] = connect_speed
            item['alive_time'] = alive_time

            yield item

        if self.page < 100:
            self.page += 1

        yield scrapy.Request(self.base_url % self.page,callback=self.parse)

    def getVal(self,data):
        return data[0] if data else ''
