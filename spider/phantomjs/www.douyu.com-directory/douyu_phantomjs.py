#coding:utf8
from selenium import webdriver
import time,json
from bs4 import BeautifulSoup

browser = webdriver.PhantomJS()

browser.get('https://www.douyu.com/directory/all')
time.sleep(3)

while True:

    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')

    lists_div = soup.select('ul[class*="play-list"] li')

    with open('douyu_phantomjs.json','a') as f:
        for item in lists_div:
            li_list = {}
            li_list['title'] = item.select("h3")[0].text.strip()
            li_list['class'] = item.select('span[class*="tag ellipsis"]')[0].text
            li_list['dyname'] = item.select('span[class*="dy-name ellipsis fl"]')[0].text
            dynum = item.select('span[class*="dy-num fr"]')
            if dynum:
                li_list['dynum'] = item.select('span[class*="dy-num fr"]')[0].text

            f.write(json.dumps(li_list,ensure_ascii=False).encode('utf8')+'\n')

        #判断下一页不可点击则跳出循环
        next = 'shark-pager-disable-next'
        is_next = browser.page_source.find(next)
        print is_next,type(is_next)
        if is_next != -1:
            break

        browser.find_element_by_class_name('shark-pager-next').click()
        time.sleep(0.5)