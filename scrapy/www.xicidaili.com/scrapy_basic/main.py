# -*- coding: utf-8 -*-

from scrapy import cmdline
# 西刺代理
cmdline.execute("scrapy crawl xici_scrapy".split())
# cmdline.execute("scrapy crawl xici_scrapy -o xici.csv".split())