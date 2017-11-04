#coding:utf8

import threading
import Queue
import time,random
import requests
from lxml import etree
import json

#机器人数量
concurrent = 3
parse_count = 3

#执行采集线程
class CrawlThread(threading.Thread):
    def __init__(self,task_q,data_q,num):
        super(CrawlThread,self).__init__()
        self.num = num + 1
        self.task_q = task_q
        self.data_q = data_q
        self.sess = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        self.sess.headers = self.headers

    def run(self):
        print '启动面壁人%d号' % self.num
        # 队列长度大于0
        while self.task_q.qsize() > 0:
            url = self.task_q.get()
            print '%d号面壁人采集%s' % (self.num,url)

            time.sleep(random.randint(3,4))
            response = self.sess.get(url)
            html = response.text
            self.data_q.put(html)
        print '结束面壁人%d号' % self.num

#执行解析线程
class ParseThead(threading.Thread):
    def __init__(self,data_q,crawl_list,num,lock,f):
        super(ParseThead,self).__init__()
        self.data_q = data_q
        self.crawl_list = crawl_list
        self.num = num + 1
        # 是否解析
        self.is_parse = True
        self.lock = lock
        self.f = f

    def run(self):
        print '启动破壁人%d号' % self.num
        while True:
            for crawl in self.crawl_list:
                if crawl.is_alive():
                    break
                else:
                    # 数据队列为空，并且所有采集线程执行完毕
                    if self.data_q.qsize() == 0:
                        self.is_parse = False

            if self.is_parse:
                try:
                    html = self.data_q.get(timeout = 3)
                    self.parse(html)
                except Exception,e:
                    pass
            else:
                break
        print '结束破壁人%d号' % self.num

    def parse(self,html):
        html = etree.HTML(html)
        duanzi_div = html.xpath('//div[@id="content-left"]/div')
        for duanzi in duanzi_div:
            item = {}
            item['nick'] = duanzi.xpath('.//h2')[0].text
            age = duanzi.xpath('.//div[@class="articleGender manIcon"] | .//div[@class="articleGender womenIcon"]')
            if age:
                item['age'] = age[0].text
            item['content'] = duanzi.xpath('.//div[@class="content"]/span')[0].text.replace('\n','')
            item['votes'] = duanzi.xpath('.//span[@class="stats-vote"]/i')[0].text
            item['comments'] = duanzi.xpath('.//span[@class="stats-comments"]//i')[0].text
            item['imgs'] = duanzi.xpath('.//div[@class="thumb"]//img/@src')
            print item
            with self.lock:
                self.f.write(json.dumps(item,ensure_ascii=False).encode('utf8')+'\n')

def main():
    #任务队列
    task_q = Queue.Queue()

    # 数据队列
    data_q = Queue.Queue()

    # 锁
    lock = threading.Lock()

    #打开文件对象
    f = open('qiushi_data.json','w')

    #生成10个任务追加到任务队列里
    for i in range(1,11):
        url = 'https://www.qiushibaike.com/8hr/page/%d/' % i
        task_q.put(url)

    # 启动采集线程
    crawl_list = []
    for num in range(concurrent):
        t = CrawlThread(task_q,data_q,num)
        t.start()
        crawl_list.append(t)

    #启动解析线程
    parse_list = []
    for num in range(parse_count):
        t = ParseThead(data_q,crawl_list,num,lock,f=f)
        t.start()
        parse_list.append(t)

    # 等待所有采集线程运行完毕
    for crawl in crawl_list:
        crawl.join()

    # 等待所有解析线程运行完毕
    for parse in parse_list:
        parse.join()

    f.close()

if __name__ == '__main__':
    start = time.time()
    main()
    print 'resume',time.time()-start


