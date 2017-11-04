# -*- coding: utf-8 -*-
import scrapy
from qunar.items import QunarItem

from lxml import etree
import requests

class QunarSpiderSpider(scrapy.Spider):
    name = 'qunar_spider'
    allowed_domains = ['hotel.qunar.com']
    # Q居
    start_urls = ['http://qju.hotel.qunar.com/cities/']
    # Q+
    # start_urls = ['http://qunarplus.hotel.qunar.com/cities/']

    def parse(self, response):
        # html = response.body

        urls = response.xpath('//div[@class="b_internal"]//li/a/@href').extract()
        for qju_url in urls:
            # print qju_url

            yield scrapy.Request(url=qju_url,callback=self.parse_urls)

    def parse_urls(self,response):
        # data_page = self.getVal(response.xpath('//div[@class="q_page"]//div[@class="pager"]/a/@data-page').extract())
        # for page in range(1,5):
        for page in range(1,37):
            if page == 1:
                full_urls=response.url
            else:
                full_urls = response.url+'p' + str(page) + '.html'
            print full_urls
            print '+'*200
            html = requests.get(full_urls)
            xml = etree.HTML(html.content)
            hotel_cont =xml.xpath('//div[@class="b_main"]/ul/li[@class="e_item"]')
            item = QunarItem()
            for hotel_item in hotel_cont:
                hotel_name = hotel_item.xpath('.//div[@class="message"]//dl/dt/a/text()')
                hotel_url = hotel_item.xpath('.//div[@class="message"]//dl/dt/a/@href')
                hotel_intr = self.getVal(hotel_item.xpath('.//div[@class="message"]//dl/dd/text()'))
                hotel_price1 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/em/text()'))
                hotel_price2 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/strong/text()'))
                hotel_price3 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/i/text()'))
                hotel_price = hotel_price1 + hotel_price2 + hotel_price3
                hotel_score1 = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]//span[@class="score"]/a/em/text()'))
                hotel_score2 = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]//span[@class="score"]/a/text()'))
                hotel_score = hotel_score1 + hotel_score2
                hotel_comment = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]/div[@class="comment"]/a[1]/text()'))
                hotel_rank = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]/div[@class="comment"]/div[@class="rank"]/text()'))

                # print hotel_name,hotel_url,hotel_intr,hotel_price,hotel_score,hotel_comment,hotel_rank

                item['hotel_name'] = hotel_name
                item['hotel_url'] = hotel_url
                item['hotel_intr'] = hotel_intr
                item['hotel_price'] = hotel_price
                item['hotel_score'] = hotel_score
                item['hotel_comment'] = hotel_comment
                item['hotel_rank'] = hotel_rank


                yield item



    # def parse_list(self,response):
    #     print response.url
    #     print '*'*200
    #     hotel_cont =response.xpath('//div[@class="b_main"]/ul/li[@class="e_item"]')
    #     item = QunarItem()
    #
    #     for hotel_item in hotel_cont:
    #         hotel_name = hotel_item.xpath('.//div[@class="message"]//dl/dt/a/text()').extract()[0]
    #         hotel_url = hotel_item.xpath('.//div[@class="message"]//dl/dt/a/@href').extract()[0]
    #         hotel_intr = self.getVal(hotel_item.xpath('.//div[@class="message"]//dl/dd/text()').extract())
    #         hotel_price1 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/em/text()').extract())
    #         hotel_price2 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/strong/text()').extract())
    #         hotel_price3 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/i/text()').extract())
    #         hotel_price = hotel_price1 + hotel_price2 + hotel_price3
    #         hotel_score1 = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]//span[@class="score"]/a/em/text()').extract())
    #         hotel_score2 = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]//span[@class="score"]/a/text()').extract())
    #         hotel_score = hotel_score1 + hotel_score2
    #         hotel_comment = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]/div[@class="comment"]/a[1]/text()').extract())
    #         hotel_rank = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]/div[@class="comment"]/div[@class="rank"]/text()').extract())
    #
    #         print hotel_name,hotel_url,hotel_intr,hotel_price,hotel_score,hotel_comment,hotel_rank
    #
    #         item['hotel_name'] = hotel_name
    #         item['hotel_url'] = hotel_url
    #         item['hotel_intr'] = hotel_intr
    #         item['hotel_price'] = hotel_price
    #         item['hotel_score'] = hotel_score
    #         item['hotel_comment'] = hotel_comment
    #         item['hotel_rank'] = hotel_rank
    #
    #
    #         yield item


    def getVal(self,data):
        return data[0] if data else ''

