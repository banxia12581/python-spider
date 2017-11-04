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

