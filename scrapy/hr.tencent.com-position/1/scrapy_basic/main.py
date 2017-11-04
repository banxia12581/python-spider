# -*- coding: utf-8 -*-

from scrapy import cmdline

# 腾讯招聘代理
# cmdline.execute("scrapy crawl tencent_scrapy".split())

cmdline.execute("scrapy crawl tencent_scrapy -o hr-tencent.csv".split())