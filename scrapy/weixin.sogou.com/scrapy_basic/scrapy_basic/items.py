# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBasicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CdblogsItem(scrapy.Item):
    blogs_name = scrapy.Field()
    blogs_desc = scrapy.Field()
    blogs_title = scrapy.Field()
    blogs_img = scrapy.Field()
    #图片路径
    blogs_imgpath = scrapy.Field()
    blogs_comment = scrapy.Field()
    blogs_date = scrapy.Field()
    blogs_view = scrapy.Field()
    blogs_url = scrapy.Field()
    blogs_cont = scrapy.Field()

class BloggerItem(scrapy.Item):
    author = scrapy.Field()
    blogger_article = scrapy.Field()
    blogger_date = scrapy.Field()
    blogger_class = scrapy.Field()
    blogger_view = scrapy.Field()
    blogger_comment = scrapy.Field()
    blogger_href = scrapy.Field()
    blogger_desc = scrapy.Field()
    blogger_cont = scrapy.Field()

class WeiSogoItem(scrapy.Item):
    news_article = scrapy.Field()
    news_account = scrapy.Field()
    news_desc = scrapy.Field()
    news_href = scrapy.Field()
    news_date =  scrapy.Field()
    news_cont = scrapy.Field()

class TencentCrawlItem(scrapy.Item):
    position_name = scrapy.Field()
    location = scrapy.Field()
    position_type = scrapy.Field()
    position_num = scrapy.Field()
    position_duty =  scrapy.Field()
    position_url = scrapy.Field()
    requestion =  scrapy.Field()
