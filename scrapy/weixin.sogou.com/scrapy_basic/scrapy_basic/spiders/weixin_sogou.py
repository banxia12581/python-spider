# -*- coding: utf-8 -*-
import scrapy
from scrapy_basic.items import WeiSogoItem

class WeixinSogouSpider(scrapy.Spider):
    name = 'weixin_sogou'
    allowed_domains = ['weixin.sogou.com']
    page = 0
    start_urls = ['http://weixin.sogou.com/']
    base_url = 'http://weixin.sogou.com/'


    def parse(self, response):
        news_list = response.xpath('//li[@d]')
        for news_item in news_list:
            news_article = news_item.xpath('.//h3/a/text()').extract()[0]
            news_account = news_item.xpath('.//div[@class="s-p"]/a[@class="account"]/text()').extract()[0]
            news_desc = news_item.xpath('.//p[@class="txt-info"]/text()').extract()[0]
            news_href = news_item.xpath('.//h3/a/@href').extract()[0]

            info = {
                'news_article':news_article,
                'news_account':news_account,
                'news_desc':news_desc,
                'news_href':news_href,
            }
            yield scrapy.Request(url=news_href,callback=self.parse_article,meta=info,dont_filter=True)
        if self.page == 0:
            yield scrapy.Request(self.base_url,callback=self.parse)
            print self.base_url
            print '-' * 200

        self.page += 1
        print self.page
        if self.page > 0:
            while self.page < 4:

                yield scrapy.Request(self.base_url + '/pcindex/pc/pc_0/' + str(self.page) + '.html',callback=self.parse)
                print self.base_url + '/pcindex/pc/pc_0/' + str(self.page) + '.html'
                print '-+' * 200

                self.page += 1


    # 解析文章详情
    def parse_article(self,response):
        item = WeiSogoItem()
        news_article = response.meta['news_article']
        news_account = response.meta['news_account']
        news_desc = response.meta['news_desc']
        news_href = response.meta['news_href']
        news_date =  response.xpath('//em[@id="post-date"]/text()').extract()
        news_date = self.getVal(news_date)
        news_cont = response.xpath('//div[@id="js_content"]//p//text()').extract()[0:-1]

        item['news_article'] = news_article
        item['news_account'] = news_account
        item['news_desc'] = news_desc
        item['news_href'] = [news_href]
        item['news_date'] = news_date
        item['news_cont'] = news_cont

        print news_cont

        yield item
        # print item

    # 没有匹配到结果 则返回空
    def getVal(self,data):
        return data[0] if data else ''
