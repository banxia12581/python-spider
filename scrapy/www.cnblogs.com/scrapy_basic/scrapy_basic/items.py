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


