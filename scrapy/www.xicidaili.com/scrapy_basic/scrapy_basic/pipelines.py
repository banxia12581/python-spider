# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo

#公共
class CommonPipeline(object):
    #必须要实现的方法 处理item
    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False).encode('utf8')+'\n')
        return item
    def close_spider(self,spider):
        self.f.close()

class SpiderBasicPipeline(object):
    def process_item(self, item, spider):
        return item

class ProxyPipeline(CommonPipeline):
    #必须要实现的方法 处理item
    def __init__(self):
        self.f = open('xici_scrapy.json','w')

class MongoDBPipeline(object):
    # 初始化
    def __init__(self):
        try:
            # 建立连接
            self.mongoclient = pymongo.MongoClient(host = '192.168.2.218',port=27017)
            # 指定操作数据库
            self.db = self.mongoclient['mymongodb']
            # 指定操作表（collection）
            self.sheet = self.db['proxy_db']

        except Exception,e:
            print '数据库连接失败'
            print str(e)
    def process_item(self,item,spider):
        print dict(item)
        try:
            # sql = {"alive_time": "%s", "addr": "%s", "http_type": "%s", "location": "%s", "speed": "%s", "ip_port": "%s", "connect_speed": "%s"}
            self.sheet.insert(dict(item))
        except Exception,e:
            print '插入失败',str(e)

        return item


