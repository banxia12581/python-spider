#coding:utf8
import json
import redis
import MySQLdb

def main():
    # 指定redis数据库信息
    try:
        rediscli = redis.StrictRedis(host='192.168.1.108', port=6379, db=0)
        # 指定mysql数据库
        mysqlcli = MySQLdb.connect(host='192.168.1.108', user='centos4', passwd='123456', db = 'mydb', port=3306, charset='utf8')
    except Exception,e:
        print '数据库连接失败'
        print str(e)
        exit()

    while True:
        source, data = rediscli.blpop(["love:items"])
        # print source # redis里的键
        # print data # 返回的数据
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            sql = "insert into truelove(nick, age,crawled, spider,url) values('%s',%s, '%s', '%s','%s') on duplicate key update " \
                  "nick=values(nick),age=values(age),crawled=values(crawled),spider=values(spider)" % (item['nick'], item['age'], item['crawled'], item['spider'],item['url'])

            cur.execute(sql)
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print "inserted %s" % item['nick']
        except Exception,e:
            print '插入失败'
            print str(e)

if __name__ == '__main__':
    main()