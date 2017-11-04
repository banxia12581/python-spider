# -*- coding: utf-8 -*-

from scrapy import cmdline

# 搜狗公众号
cmdline.execute("scrapy crawl weixin_sogou -o weixin.csv".split())
# cmdline.execute("scrapy crawl weixin_sogou".split())

