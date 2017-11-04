# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline
import MySQLdb
import hashlib
# 异步数据库操作api
from twisted.enterprise import adbapi
import MySQLdb.cursors

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

# 保存图片的Pipeline
class CnblogsImagePipeline(ImagesPipeline):

    def item_completed(self, results, item, info):
        # 图片处理结果
        status = results[0][0]
        if status:
            item['blogs_imgpath'] = results[0][1]['path']
        else:
            item['blogs_imgpath'] = ''
        return item

# 数据库操作相关
def getMd5(data):
    m = hashlib.md5()
    m.updata(data)
    return m.hexdigest()


# 同步写入mysql
class CnblogsMysqlPipeline(object):
    # 初始化
    def __init__(self):
        try:
            self.conn = MySQLdb.connect('127.0.0.1','root','','mydb',charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception,e:
            print '数据库连接失败'
            print str(e)

    def process_item(self,item,spider):
        sql = 'insert into cnblogs(blogs_name,blogs_desc,blogs_title,blogs_imgpath,blogs_comment,blogs_date,blogs_view,blogs_url,blogs_cont)'\
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE '\
              ' blogs_url=values(blogs_url)'
        try:
            self.cursor.execute(sql,(item['blogs_name'],item['blogs_desc'],item['blogs_title'],item['blogs_imgpath'],item['blogs_comment'],item['blogs_date'],item['blogs_view'],item['blogs_url'],item['blogs_cont']))
            self.conn.commit()
        except Exception,e:
            print '插入失败',str(e)

        return item


    # 最后调用
    def close_spider(self):
        self.cursor.close()
        self.conn.close()

# 数据库异步
class TwistedMysqlPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    # 方法名是固定的
    # 类方法 静态方法 先加载类静态方法，优先__init__执行
    @classmethod
    def from_settings(cls,settings):
        db_config = dict(
            host = settings['MYHOST'],
            user = settings['MYUSER'],
            passwd = settings['MYPASSWORD'],
            db = settings['MYDB'],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb',**db_config)
        return cls(dbpool)

    def process_item(self,item,spider):
        # 异步插入操作
        query = self.dbpool.runInteraction(self.insert,spider)
        query.addErrback(self.haddle_error)
        return item

    # 插入操作
    # 腾讯招聘
    def insert(self,cursor,item):
        print dict(item)
        print '-'*200
        sql = 'insert into cnblogs3(blogs_name,blogs_desc,blogs_title,blogs_imgpath,blogs_comment,blogs_date,blogs_view,blogs_url,blogs_cont)'\
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE '\
              ' blogs_url=values(blogs_url)'
        try:
            self.cursor.execute(sql,(item['blogs_name'],item['blogs_desc'],item['blogs_title'],item['blogs_imgpath'],item['blogs_comment'],item['blogs_date'],item['blogs_view'],item['blogs_url'],item['blogs_cont']))
            print '插入数据库成功'
        except Exception,e:
            print '插入失败',str(e)

    # 错误处理函数
    def haddle_error(self,error):
        print str(error)



