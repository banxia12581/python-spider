from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from example.items import HaoItem

class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'hao'
    # allowed_domains = ['dmoztools.net']
    start_urls = ['http://www.hao123.com']

    rules = [
        Rule(LinkExtractor(), callback='parse_directory', follow=False),
    ]

    def parse_directory(self, response):
        item = HaoItem()
        title = response.xpath('//title/text()').extract()[0]
        url = response.url
        item['title'] = title
        item['url'] = url
        yield  item