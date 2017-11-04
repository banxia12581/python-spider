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


class TencentCrawlItem(scrapy.Item):
    position_name = scrapy.Field()
    location = scrapy.Field()
    position_type = scrapy.Field()
    position_num = scrapy.Field()
    position_duty =  scrapy.Field()
    position_url = scrapy.Field()
    requestion =  scrapy.Field()
