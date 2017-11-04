# -*- coding: utf-8 -*-
import scrapy
from qunar.items import QunarItem

class QunarSpiderSpider(scrapy.Spider):
    name = 'qunar_spider'
    allowed_domains = ['hotel.qunar.com']
    start_urls = ['http://pinpai.hotel.qunar.com/']


    def parse(self, response):
        '''

        :获取品牌页面所有品牌酒店链接
        :return:每个品牌链接下的页面
        '''
        urls = response.xpath('//div[@class="hsort_wrap"]//ul[@class="clr_after"]/li[@class="item"]/dl/dt/a/@href').extract()
        for pinpai_url in urls:
            # print pinpai_url
            yield scrapy.Request(url=pinpai_url,callback=self.parse_allurl)

    def parse_allurl(self,response):
        '''
        :单个品牌首页
        :return: 获取该品牌链接下的全部地区列表页
        '''
        all_urls = self.getVal(response.xpath('//div[@class="q_page"]//div[@class="b_main"]/div[@class="b_menu"]/ul/li[@class="more"]/a/@href').extract())
        if all_urls:
            yield scrapy.Request(url=all_urls,callback=self.parse_urls)

    def parse_urls(self, response):
        '''
        :单个品牌下的全部地区列表页
        :return:单个地区的全部酒店列表页
        '''
        urls = response.xpath('//div[@class="b_internal"]//li/a/@href').extract()
        # print urls,type(urls)
        if urls:
            for pp_url in urls:
                # print pp_url
                yield scrapy.Request(url=pp_url,callback=self.parse_pages)

    def parse_pages(self,response):
        '''
        :分页操作
        '''
        data_page = self.getVal(response.xpath('//div[@class="q_page"]//div[@class="pager"]/a/@data-page').extract())
        if data_page:
            page_end = int(data_page)+1
            for page in range(1,page_end):
                full_urls = response.url+'p' + str(page) + '.html'
                yield scrapy.Request(url=full_urls,callback=self.parse_list,priority=1)
        else:
            # page_end =response.xpath('//div[@class="q_page"]//div[@class="pager"]/em/text()').extract()[0].encode('utf8')
            # print page_end,type(page_end)
            full_urls = response.url
            yield scrapy.Request(url=full_urls,callback=self.parse_list,priority=1)


    def parse_list(self,response):
        '''
        :用xpath解析数据
        :return: 数据字典
        '''
        hotel_cont =response.xpath('//div[@class="b_main"]/ul/li[@class="e_item"]')
        item = QunarItem()

        for hotel_item in hotel_cont:
            hotel_name = hotel_item.xpath('.//div[@class="message"]//dl/dt/a/text()').extract()[0]
            hotel_url = hotel_item.xpath('.//div[@class="message"]//dl/dt/a/@href').extract()[0]
            hotel_intr = self.getVal(hotel_item.xpath('.//div[@class="message"]//dl/dd/text()').extract())
            hotel_price1 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/em/text()').extract())
            hotel_price2 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/strong/text()').extract())
            hotel_price3 = self.getVal(hotel_item.xpath('.//div[@class="message"]//div[@class="price"]/a/i/text()').extract())
            hotel_price = hotel_price1 + hotel_price2 + hotel_price3
            hotel_score1 = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]//span[@class="score"]/a/em/text()').extract())
            hotel_score2 = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]//span[@class="score"]/a/text()').extract())
            hotel_score = hotel_score1 + hotel_score2
            hotel_comment = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]/div[@class="comment"]/a[1]/text()').extract())
            hotel_rank = self.getVal(hotel_item.xpath('.//div[@class="bottom_area"]/div[@class="comment"]/div[@class="rank"]/text()').extract())

            print hotel_name,hotel_url,hotel_intr,hotel_price,hotel_score,hotel_comment,hotel_rank

            item['hotel_name'] = hotel_name
            item['hotel_url'] = hotel_url
            item['hotel_intr'] = hotel_intr
            item['hotel_price'] = hotel_price
            item['hotel_score'] = hotel_score
            item['hotel_comment'] = hotel_comment
            item['hotel_rank'] = hotel_rank


            yield item


    def getVal(self,data):
        return data[0] if data else ''

