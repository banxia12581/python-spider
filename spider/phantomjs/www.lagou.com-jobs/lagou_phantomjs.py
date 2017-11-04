#coding:utf8

from selenium import webdriver
import time,json
from lxml import etree


# 加useragent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
)
browser = webdriver.PhantomJS(desired_capabilities=dcap)

browser.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')
time.sleep(1)

with open('lagou_phantomjs.json','w') as f:
    while True:
        html = browser.page_source
        html = etree.HTML(html)
        position_list = html.xpath('//div[@id="s_position_list"]//ul[@class="item_con_list"]//li')
        for position in position_list:
            item = {}
            item['position_name'] = position.xpath('.//h3')[0].text
            item['format_time'] = position.xpath('.//span[@class="format-time"]')[0].text
            item['position_money'] = position.xpath('.//span[@class="money"]')[0].text
            item['company_name'] = position.xpath('.//div[@class="company_name"]//a')[0].text
            item['location'] = position.xpath('.//span[@class="add"]//em')[0].text
            f.write(json.dumps(item,ensure_ascii=False).encode('utf8')+'\n')

        #判断下一页不可点击则跳出循环
        is_next = browser.page_source.find('pager_next pager_next_disabled')
        if is_next != -1:
            break
        browser.find_element_by_class_name('pager_next').click()
        time.sleep(0.5)

