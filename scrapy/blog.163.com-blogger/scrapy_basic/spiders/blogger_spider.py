# -*- coding: utf-8 -*-
import scrapy
import random
from scrapy_basic.items import BloggerItem
import re,os,json


class BloggerSpiderSpider(scrapy.Spider):
    name = 'blogger_spider'
    allowed_domains = ['blog.163.com']
    start_urls = ['http://blog.163.com/blogger.html']
    base_url = 'http://blog.163.com/blogger.html'
    def __int__(self):
        self.hao=0

    # 名博页面解析
    def parse(self, response):
        author_list = response.xpath('//div[@class="g-bd ui-bg2"]//ol/li/a/@href').extract()[:5]
        author = response.xpath('//div[@class="g-bd ui-bg2"]//ol/li/a/text()').extract()[:5]

        pattern = re.compile(r'http://(.+)\.blog\.163.com')
        blog_list = []
        for author_item in author_list:
            author_exit = pattern.findall(author_item)
            blog_list.append(author_exit)

            print author_item
            print '-' * 200
            info = {
                'author':author,
            }

            yield scrapy.Request(url=author_item,callback=self.author_blog_index,meta=info)

        for j in range(0,len(blog_list)):
            if blog_list[j]:
                try:
                    dirname=author[j]+blog_list[j][0]
                    os.makedirs('./blogger/'+dirname)
                except:
                    continue
            else:
                dirname = author[j]
                os.makedirs('./blogger/' + dirname)


    # 解析该博主fromBlogger
    def author_blog_index(self, response):
        author_name = response.url.split('/')[2].split('.')[0]
        author = response.meta['author']
        str=response.xpath("//a[@class='m2a fc03 fs1 ztag']/@href").extract()[0]
        pattern=re.compile(r'static/(\d{9})')
        hao=pattern.findall(str)[0].encode('utf-8')
        index_info ={
            'author':author,
            'author_name':author_name,
            'hao':hao,
        }
        blog_list_href = response.xpath('//p[@class="lnk"]/a/@href').extract()[0]
        print blog_list_href
        print '-+' * 200
        yield scrapy.Request(url=blog_list_href,callback=self.author_blog_list,meta=index_info)


    # 解析该博主微博列表页面api
    def author_blog_list(self, response):
        hao = response.meta['hao'].encode('utf-8')
        author_name = response.meta['author_name'].encode('utf-8')
        blog_list_href = 'http://api.blog.163.com/'+author_name+'/dwr/call/plaincall/BlogBeanNew.getBlogs.dwr'
        print blog_list_href
        author=response.meta['author']
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
            'Content-Type': 'text/plain',
            'Referer': 'http://api.blog.163.com/crossdomain.html?t=20100205',
        }
        list_info ={
            'author':author,
            'author_name':author_name,
        }
        yield scrapy.FormRequest(
            url=blog_list_href,
            formdata={
                'callCount':'1',
                'scriptSessionId':'${scriptSessionId}187',
                'c0-scriptName':'BlogBeanNew',
                'c0-methodName':'getBlogs',
                'c0-id':'0',
                'c0-param0':hao,
                'c0-param1':'0',
                'c0-param2':'20',
                'batchId':'1',
            },
            headers=headers,
            callback=self.parse_article,
            meta=list_info,
        )

    # 解析列表页api内容
    def parse_article(self,response):
        author_name = response.meta['author_name']
        author=response.meta['author']
        article_info ={
            'author':author,
            'author_name':author_name,
        }
        num_parrent = re.compile(r's\d+\.permaSerial="(.*?)"')
        article_nums = num_parrent.findall(response.body)

        for num in article_nums:
            article_url = 'http://'+author_name+'.blog.163.com/blog/static/'+str(num)
            print article_url
            print '#'*200
            yield scrapy.Request(url=article_url,callback=self.parse_detial,meta=article_info)

    #  解析文章详情
    def parse_detial(self,response):
        author_name = response.meta['author_name']
        article_title = response.xpath('//span[@class="tcnt"]/text()').extract()[0]
        article_cont = response.xpath('//div[@class="bct fc05 fc11 nbw-blog ztag"]//text()').extract()
        dir_list = os.listdir('./blogger')
        dir_parrent = re.compile(author_name)
        print response.url,article_cont

        for dir_i in dir_list:
            print dir_i
            if dir_parrent.search(dir_i):
                with open('./blogger/'+dir_i.decode('gbk')+'/'+article_title+'.json','w') as f:
                # with open('./blogger/'+dir_i.decode('gbk')+'/'+article_title+'.csv','w') as f:
                    f.write(json.dumps(article_cont,ensure_ascii=False).encode('utf8')+'\n')
            else:
                pass

    #输入数字
    def getNum(self,data):
        return int(data.strip().split('(')[1].split(')')[0])




