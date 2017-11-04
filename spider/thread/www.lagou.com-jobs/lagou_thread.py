#coding:utf8

import requests
import json
import jsonpath
from bs4 import BeautifulSoup
import threading
import Queue
import random,time

concurrent = 3
parse_count = 3

headers = {
        'Origin':'https://www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python',
        'Host':'www.lagou.com',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8',
}

#执行采集线程
class CrawlThread(threading.Thread):
    def __init__(self,takd_q,data_q,num):
        super(CrawlThread,self).__init__()
        self.num = num + 1
        self.task_q = takd_q
        self.data_q = data_q

    def run(self):
        print '启动面壁人%d号' % self.num
        while self.task_q.qsize() > 0:
            url = self.task_q.get()
            print '%d号面壁人采集%s' % (self.num,url)

            time.sleep(random.randint(3,4))
            response = requests.get(url,headers=headers)
            html = response.content
            print html
            self.data_q.put(html)

        print '结束面壁人%d号' % self.num

#执行解析线程
class ParseThread(threading.Thread):
    def __init__(self,data_q,crawl_list,num,lock,f):
        super(ParseThread,self).__init__()
        self.data_q = data_q
        self.crawl_list = crawl_list
        self.num = num + 1
        self.lock = lock
        self.f = f
        # 是否解析
        self.is_parse = True
    def run(self):
        print '启动破壁人%d号' % self.num
        while True:
            for crawl in self.crawl_list:
                if crawl.is_alive():
                    break
                else:
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

        for i in range(int(1),int(1)+1):
            html = json.loads(html)
            res = jsonpath.jsonpath(html,'$..positionResult..result..*')

            with self.lock:
                self.f.write(json.dumps(res,ensure_ascii=False).encode('utf8')+'\n')

def main():
    task_q = Queue.Queue()

    data_q = Queue.Queue()

    lock = threading.Lock()

    f = open('lagou_thread.json','w')
    for i in range(1,2):
        url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0&first=true&kd=python&pn=' + str(i)
        task_q.put(url)

    crawl_list = []
    for num in range(concurrent):
        t = CrawlThread(task_q,data_q,num)
        t.start()
        crawl_list.append(t)

    parse_list = []
    for num in range(parse_count):
        t = ParseThread(data_q,crawl_list,num,lock,f=f)
        t.start()
        parse_list.append(t)

    for crawl in crawl_list:
        crawl.join()

    for parse in parse_list:
        parse.join()

if __name__ == '__main__':
    start = time.time()
    main()
    print 'resume',time.time()-start