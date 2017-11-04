#coding:utf8
from selenium import webdriver #引入浏览器驱动
from selenium.webdriver.common import keys
import time

#创造一个浏览器
browser1 = webdriver.PhantomJS()  # //内核 webkkit
browser1.get('https://www.xinhucaifu.com/product.php?t=rxcp&search[iptype]=&search[ratetype]=&search[siatype]=&search[type]=&search[status]=&search[order]=&search[name]=&page=1')

# print browser1.page_source
browser1.find_element_by_class_name('veria1').click()
time.sleep(2)

print browser1.page_source
