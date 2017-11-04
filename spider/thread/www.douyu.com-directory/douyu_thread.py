#coding:utf8

import requests
import json
from bs4 import BeautifulSoup

import threading
import Queue
import time,random

#机器人数量
concurrent = 3
parse_count = 3

#执行采集线程
class CrawlThread(threading.Thread):
    def __init__(self,task_q,data_q,num):
        super(CrawlThread,self).__init__()
        self.num = num + 1
        self.data_q = data_q
        self.task_q = task_q


    def run(self):
        print '启动面壁人%d号' % self.num
        while self.task_q.qsize() > 0:
            url = self.task_q.get()
            print '%d号面壁人采集%s' % (self.num,url)

            #由于解析速度慢于采集速度,所以采集之后停止3秒
            time.sleep(random.randint(3,4))

            response = requests.get(url)
            html = response.text
            self.data_q.put(html)
            print '结束面壁人%d号' % self.num


#执行解析线程
class ParseThread(threading.Thread):
    def __init__(self,data_q,crawl_list,num,lock,f):
        super(ParseThread,self).__init__()
        self.num = num + 1
        self.data_q = data_q
        self.crawl_list = crawl_list
        self.f = f
        #是否解析
        self.is_parse = True
        self.lock = lock

    def run(self):
        print '启动破壁人%d号' % self.num
        while True:
            for crawl in self.crawl_list:
                if crawl.is_alive():
                    break
                else:
                    #数据队列为空，并且所有采集线程执行完毕
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
        soup = BeautifulSoup(html,'lxml')
        lists_div = soup.select('ul[class*="play-list"] li')
        print lists_div
        for item in lists_div:
            li_list = {}
            li_list['title'] = item.select("h3")[0].text.strip()
            li_list['class'] = item.select('span[class*="tag ellipsis"]')[0].text
            li_list['dyname'] = item.select('span[class*="dy-name ellipsis fl"]')[0].text
            dynum = item.select('span[class*="dy-num fr"]')
            if dynum:
                li_list['dynum'] = item.select('span[class*="dy-num fr"]')[0].text
            # print li_list['title']
            if self.lock:
                self.f.write(json.dumps(li_list,ensure_ascii=False).encode('utf8')+'\n')


def main():
    #任务队列
    task_q = Queue.Queue()

    #解析队列
    data_q = Queue.Queue()

    #锁
    lock = threading.Lock()

    #打开文件对象
    f = open('douyu_thread.json','w')

    #生成10个任务到队列里面
    for i in range(1,2):
        url = 'https://www.douyu.com/directory/all?page='+str(i)
        task_q.put(url)

    #启动采集任务
    crawl_list = []
    for num in range(concurrent):
        t = CrawlThread(task_q,data_q,num)
        t.start()
        crawl_list.append(t)

    #启动解析任务
    parse_list = []
    for num in range(parse_count):
        t = ParseThread(data_q,crawl_list,num,lock,f=f)
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
    print 'redone',time.time()-start