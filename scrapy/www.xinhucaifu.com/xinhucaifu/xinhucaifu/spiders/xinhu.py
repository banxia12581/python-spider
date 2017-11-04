# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

header = {
    'Accept':'text/plain, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'PHPSESSID=3gldcss1i2ncge9jaf1tss3180; BIGipServerwww.xinhucaifu.com=3355551936.10531.0000; Hm_lvt_8542dcfc4765cc3e5e08fcb4da5655cf=1509497868; Hm_lpvt_8542dcfc4765cc3e5e08fcb4da5655cf=1509497884',
    'Host':'www.xinhucaifu.com',
    'Referer':'https://www.xinhucaifu.com/product.php?t=rxcp',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

class XinhuSpider(scrapy.Spider):
    name = 'xinhu'
    allowed_domains = ['www.xinhucaifu.com']
    page = 1
    base_url = 'https://www.xinhucaifu.com/product.php?t=rxcp&search[iptype]=&search[ratetype]=&search[siatype]=&search[type]=&search[status]=&search[order]=&search[name]=&page=%d'
    start_urls = [base_url % page]

    def get_cookies(self):
        fir_url = 'https://www.xinhucaifu.com/product.php?t=rxcp'
        yield scrapy.Request(url=fir_url,callback=self.parse)

    def parse(self, response):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36"
        )
        browser = webdriver.PhantomJS(desired_capabilities=dcap)

        browser.get(response.url)

        browser.find_element_by_class_name('veria1').click()
        print browser.find_element_by_class_name('veria1')

        time.sleep(2)

        print response.body

        yield scrapy.Request(self.base_url % self.page,headers=header,callback=self.parse_detial)

    def parse_detial(self,response):
        print 2
