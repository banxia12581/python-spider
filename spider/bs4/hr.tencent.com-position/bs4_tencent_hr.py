#coding:utf8

import urllib,urllib2
from bs4 import BeautifulSoup
import json

start = raw_input('请输入开始位置:')
end = raw_input('请输入结束位置:')
for i in range(int(start),int(end)+1):
    t = (i-1) * 10
    base_url = 'http://hr.tencent.com/position.php?&start='+ str(t)
    headers = {
        'Host':'hr.tencent.com',
        'Connection':'keep-alive',
        'Pragma':'no-cache',
        'Cache-Control':'no-cache',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8',
    }

    request = urllib2.Request(base_url,headers=headers)
    response = urllib2.urlopen(request)

    htmls = BeautifulSoup(response,'lxml')
    soup = htmls.select('tr[class="even"],tr[class="odd"]')

    with open('bs4_tencent_hr.json','a') as f:
        for item in soup:
            item_list = {}
            tr_list = item.find_all('td')
            item_list['name'] = tr_list[0].text
            item_list['class'] = tr_list[1].text
            item_list['num'] = tr_list[2].text
            item_list['location'] = tr_list[3].text
            item_list['date'] = tr_list[4].text
            f.write(json.dumps(item_list,ensure_ascii=False).encode('utf8')+'\n')