# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunarItem(scrapy.Item):
    # define the fields for your item here like:
    hotel_name = scrapy.Field()
    hotel_url = scrapy.Field()
    hotel_intr = scrapy.Field()
    hotel_price = scrapy.Field()
    hotel_score = scrapy.Field()
    hotel_comment = scrapy.Field()
    hotel_rank = scrapy.Field()
