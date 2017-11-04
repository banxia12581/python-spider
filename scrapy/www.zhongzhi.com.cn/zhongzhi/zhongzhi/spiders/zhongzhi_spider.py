# -*- coding: utf-8 -*-
import scrapy
import json


class ZhongzhiSpiderSpider(scrapy.Spider):
    name = 'zhongzhi_spider'
    allowed_domains = ['zhongzhi.com.cn']
    page = 1
    base_url = 'http://www.zhongzhi.com.cn/newsattribute/news_index.json?callback=jQuery1112003903314898685517_1509584400781&num_per_page=24&show=list&channel_code=zz_hydt&business_type=news_channel&business_id=app_channel&cur_page=%d'
    start_urls = [base_url % page]

    def parse(self, response):
        data_html = response.body.split('jQuery1112003903314898685517_1509584400781(')[1].split(');')[0]
        data_json = json.loads(data_html)
        data = json.dumps(data_json,ensure_ascii=False).encode('utf8')+'\n'
        # print data
        with open('zhongzhi.json','a+') as f:
            f.write(data)


        while self.page < 2:
            self.page += 1
            yield scrapy.Request(self.base_url % self.page,callback=self.parse)




