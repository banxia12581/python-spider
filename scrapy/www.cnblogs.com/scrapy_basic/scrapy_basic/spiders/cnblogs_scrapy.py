# -*- coding: utf-8 -*-
import scrapy
from scrapy_basic.items import CdblogsItem
import time


class CdblogsScrapySpider(scrapy.Spider):
    name = 'cnblogs_scrapy'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']
    base_url = 'https://www.cnblogs.com'
    # 是否生成分页请求
    is_page = True

    def parse(self, response):

        blogs_list = response.xpath('//div[@class="post_item"]')

        for blogs in blogs_list:
            blogs_img = blogs.xpath('.//p[@class="post_item_summary"]/a/img/@src').extract()
            blogs_img = 'https:' + self.getVal(blogs_img)
            blogs_desc = blogs.xpath('.//p[@class="post_item_summary"]/text()[2]').extract()
            blogs_desc = self.getVal(blogs_desc)
            blogs_desc = self.format(blogs_desc)
            if blogs_desc == '':
                blogs_desc = blogs.xpath('.//p[@class="post_item_summary"]/text()[1]').extract()[0]
            blogs_name = blogs.xpath('.//div[@class="post_item_foot"]/a/text()').extract()[0]
            blogs_title = blogs.xpath('.//div[@class="post_item_body"]/h3/a/text()').extract()[0]
            blogs_title = self.format(blogs_title)
            blogs_url = blogs.xpath('.//div[@class="post_item_body"]/h3/a/@href').extract()[0]
            blogs_comment = blogs.xpath('.//span[@class="article_comment"]/a/text()').extract()[0]
            blogs_comment = self.getNum(blogs_comment)
            blogs_date = blogs.xpath('.//div[@class="post_item_foot"]/text()[2]').extract()[0]
            blogs_date = self.format(blogs_date)
            blogs_view = blogs.xpath('.//span[@class="article_view"]/a/text()').extract()[0]
            blogs_view = self.getNum(blogs_view)

            info = {
                'blogs_name': blogs_name,
                'blogs_desc': blogs_desc,
                'blogs_title': blogs_title,
                'blogs_img': blogs_img,
                'blogs_comment': blogs_comment,
                'blogs_date': blogs_date,
                'blogs_view': blogs_view,
                'blogs_url': blogs_url,
            }


            yield scrapy.Request(url=blogs_url,callback=self.parse_article,meta=info)

        #生成下一页请求
        # next_page_url = response.xpath('//div[@class="pager"]/a/@href').extract()[-1]
        # yield scrapy.Request(url=self.base_url + next_page_url,callback=self.parse)
        # print self.base_url + next_page_url
        # print '-' * 200

        #一次请求所有页面
        if self.is_page == True:
            for i in range(1,5):
                fullurl = self.base_url + '/sitehome/p/' + str(i)
                yield scrapy.Request(fullurl,callback=self.parse)
            self.is_page = False
            start = time.time()
            print 'redom',time.time()-start
            print '-' * 200



    #解析文章详情
    def parse_article(self,response):
        item = CdblogsItem()
        blogs_name = response.meta['blogs_name']
        blogs_desc = response.meta['blogs_desc']
        blogs_title = response.meta['blogs_title']
        blogs_img = response.meta['blogs_img']
        blogs_comment = response.meta['blogs_comment']
        blogs_date = response.meta['blogs_date']
        blogs_view = response.meta['blogs_view']
        blogs_url = response.meta['blogs_url']
        blogs_cont = response.xpath('//div[@id="post_detail"]//p/text()').extract()[0]

        item['blogs_name'] = blogs_name
        item['blogs_desc'] = blogs_desc
        item['blogs_title'] = blogs_title
        item['blogs_img'] = [blogs_img]
        item['blogs_comment'] = blogs_comment
        item['blogs_date'] = blogs_date
        item['blogs_view'] = blogs_view
        item['blogs_url'] = blogs_url
        item['blogs_cont'] = blogs_cont

        yield item

    # 没有匹配到结果 则返回空
    def getVal(self,data):
        return data[0] if data else ''

    #去掉空格和换行
    def format(self,data):
        return data.strip().replace('\n','')

    #输入数字
    def getNum(self,data):
        return int(data.strip().split('(')[1].split(')')[0])