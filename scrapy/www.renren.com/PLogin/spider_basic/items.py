# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderBasicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#西刺代理xici_scrapy.py
class ProxyItem(scrapy.Item):
    addr = scrapy.Field()
    ip_port = scrapy.Field()
    location = scrapy.Field()
    http_type = scrapy.Field()
    speed = scrapy.Field()
    connect_speed = scrapy.Field()
    alive_time = scrapy.Field()