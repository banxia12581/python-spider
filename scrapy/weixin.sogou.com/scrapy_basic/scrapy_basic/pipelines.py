# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


# 公共
class CommonPipeline(object):
    # 必须要实现的方法 处理item
    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False).encode('utf8')+'\n')
        return item
    def close_spider(self,spider):
        self.f.close()

class ScrapyBasicPipeline(object):
    def process_item(self, item, spider):
        return item

# cnblogs的Pipeline
class CnblogsPipeline(CommonPipeline):
    # 必须要实现的方法 处理item
    def __init__(self):
        self.f = open('cdblog_scrapy.json','w')

# weixin_sogou的Pipeline
class WeiSogoPipeline(CommonPipeline):
    # 必须要实现的方法 处理item
    def __init__(self):
        self.f = open('weixin_sogou.json','w')



