# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import MySQLdb

class QunarPipeline(object):
    def process_item(self, item, spider):
        return item

# 公共
class CommonPipeline(object):
    # 必须实现的方法 处理item
    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False).encode('utf8')+'\n')
        return item
    def close_spider(self,spider):
        self.f.close()


# 同步写入mysql
class QunarMysqlPipeline(object):
    # 初始化
    def __init__(self):
        try:
            self.conn = MySQLdb.connect('192.168.1.108','centos4','123456','mydb',charset='utf8')
            self.cursor = self.conn.cursor()
            print '数据库连接成功'+'\n'
        except Exception,e:
            print '数据库连接失败'
            print str(e)

    def process_item(self,item,spider):
        sql = 'insert into qunar(hotel_name,hotel_url,hotel_intr,hotel_price,hotel_score,hotel_comment,hotel_rank)'\
              'values(%s,%s,%s,%s,%s,%s,%s)'

        try:
            self.cursor.execute(sql,(item['hotel_name'],item['hotel_url'],item['hotel_intr'], item['hotel_price'] ,item['hotel_score'],item['hotel_comment'],item['hotel_rank']))
            self.conn.commit()
            print '插入成功' + sql
        except Exception,e:
            print '插入失败',str(e)
        return item

    # 最后调用
    def close_spider(self):
        self.cursor.close()
        self.conn.close()





