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


#腾讯招聘tencent_scrapy.py
class PositionItem(scrapy.Item):
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    position_num = scrapy.Field()
    location = scrapy.Field()
    date_pub = scrapy.Field()
