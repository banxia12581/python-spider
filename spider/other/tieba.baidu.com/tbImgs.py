#coding:utf-8

import urllib2,urllib
import re
import os
import sys

def saveImg(imgUrls,key,tieTit):
    '''
    :param imgUrls: 图片地址 tieTit:帖子名称 key 贴吧名称
    :return:
    '''

    #根据贴吧名称建文件
    path = './images/'+ key + '/' + tieTit

    #如果文件路径不存在,则新建文件
    if not os.path.exists(path.decode('utf8')):
        os.makedirs(path.decode('utf8'))
    #保存图片
    for imgUrl in imgUrls:
        try:
            fname = imgUrl.split('/')[-1]

            fullName = os.path.join(u'./images/',key.decode('utf8'),tieTit.decode('utf8'),fname.decode('utf8'))
            print 'downloading:'+ fullName
            urllib.urlretrieve(imgUrl,fullName)
        except:
            continue

def getImg(urlUrl,tbOneUrl):
    '''
    :param urlUrl: 获取的所有帖子的a标签里的路由/p/... tbOneUrl:帖子的实际路由
    :return:
    '''
    print tbOneUrl
    oResponse = urllib2.urlopen(tbOneUrl)
    oneHtmls = oResponse.read()

    imgPattern = re.compile(r'class="BDE_Image".*?src="(.*?)"')
    titPattern = re.compile(r'class="core_title_txt.*".*title="(.*?)"')
    imgUrls = imgPattern.findall(oneHtmls)
    tieTits = titPattern.search(oneHtmls)
    if tieTits:
        tieTit = tieTits.group(1)
    else:
        tieTit = ''

    #调用保存图片函数
    saveImg(imgUrls,key,tieTit)

def getPage(key,start,end):
    '''
    :param key: 用户输入的贴吧名称 start:想要获取的开始页位置 end=:想要获取的结束页位置
    :return:
    '''
    baseUrl = 'https://tieba.baidu.com/f?'
    qs={
        'kw':key
    }
    qs = urllib.urlencode(qs)
    for i in range(start,end+1):
        pageNum = (i - 1)*50
        urls = baseUrl+qs+'&pn='+str(pageNum)
        response = urllib2.urlopen(urls)
        htmls = response.read()

        #提取每个页面里面的所有帖子的链接
        urlPattern = re.compile(r'href="(.*?)".*class="j_th_tit "')
        urlUrls = urlPattern.findall(htmls)
        for urlUrl in urlUrls:
            print urlUrl
            tbOneUrl = 'https://tieba.baidu.com'+ urlUrl
            getImg(urlUrl,tbOneUrl)

if __name__ == '__main__':
    key = raw_input('请输入查询关键字：')
    start = raw_input('请输入想要获取的开始页数：')
    end = raw_input('请输入想要获取的结束页数：')
    getPage(key,int(start),int(end))

