#coding:utf8

from bs4 import BeautifulSoup
import requests
import json
import re

start = raw_input('请输入开始位置:')
end = raw_input('请输入结束位置:')

for i in range(int(start),int(end)+1):
    base_url = 'http://search.51job.com/list/010000,000000,0000,00,9,99,python,2,'+str(i)+'.html'

    response = requests.get(base_url)

    # 设置解码方式，转换成unicode
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'lxml')

    res = soup.select('div[class="dw_table"] div[class="el"]')
    # print res
    with open('bs4_51job.json','a') as f:
        for item in res:
            item_list = {}
            span_list = item.select('span')

            #正则匹配所有带万的字段
            salary_pattern = re.compile(u'\u4e07')
            salary_html = salary_pattern.findall(span_list[3].text)

            for salary_one in salary_html:
                if salary_one is not None:
                    #匹配-后面的数字
                    salary_over = span_list[3].text.encode('utf8').split('-')[1].split('\xe4\xb8\x87/')[0]
                    if salary_over > '1':
                        item_list['position'] = span_list[0].text.strip()
                        item_list['company'] = span_list[1].text
                        item_list['location'] = span_list[2].text
                        item_list['salary'] = span_list[3].text
                        item_list['date'] = span_list[4].text
                        # print span_list[1],len(span_list)
                        f.write(json.dumps(item_list,ensure_ascii=False).encode('utf8')+'\n')
