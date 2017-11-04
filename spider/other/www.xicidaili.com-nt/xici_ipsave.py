#coding:utf8

import urllib,urllib2
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
}
def getPage(start,end):
    baseUrl = 'http://www.xicidaili.com/nt'

    for i in range(start,end+1):
        pageUrl=baseUrl+'/'+str(end)

        request = urllib2.Request(pageUrl,headers=headers)
        response = urllib2.urlopen(request)
        xcHtml = response.read()

        #正则判断
        xcPattern = re.compile(r'<td>(.*)</td>',re.S)
        xcRes = xcPattern.findall(xcHtml)

        xcTds = [xcRes[n:n+5] for n in range(0,len(xcRes),5)]



        #将ip地址,端口号,存活时间保存到txt里
        with open('./xici/xici_ipsave'+str(i)+'.txt','w+') as f:
            for ipItem in xcTds:
                lists = 'ip为:'+ ipItem[0]+',端口号为:'+ ipItem[1] + ',存活时间:' + ipItem[3] + '\n'
                f.write(lists)


if __name__ == '__main__':
    start = raw_input('请输入开始位置:')
    end = raw_input('请输入结束位置:')
    getPage(int(start),int(end))