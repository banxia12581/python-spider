#coding=utf8

import urllib2,urllib
import json
import random,hashlib,time

#gzip解压
import gzip, os
from cStringIO import StringIO


baseUrl = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'



headers = {
    'Host':' fanyi.youdao.com',
    'Connection':' keep-alive',
    'Accept':' application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://fanyi.youdao.com',
    'X-Requested-With':' XMLHttpRequest',
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://fanyi.youdao.com/',
    'Accept-Encoding':' gzip, deflate',
    'Accept-Language':' zh-CN,zh;q=0.8',
}

content = raw_input('请输入需要翻译的内容:')


u = 'fanyideskweb'
c = str(content)
salt = str(int(time.time()*1000)+random.randint(0,10))

f = "rY0D^0'nM0}g5Mm1z%1G4"
sign = u+c+salt+f
m5 = hashlib.md5()
m5.update(sign)
sign = m5.hexdigest()
print sign

def gzip_uncompress(c_data):
    buf = StringIO(c_data)
    f = gzip.GzipFile(mode = 'rb', fileobj = buf)
    try:
        r_data = f.read()
    finally:
        f.close()
    return r_data

data ={
    'i'	: content,
    'from'	: 'AUTO',
    'to' : 'AUTO',
    'smartresult' : 'dict',
    'client' : 'fanyideskweb',
    'doctype' : 'json',
    'version' : '2.1',
    'keyfrom' : 'fanyi.web',
    'action' : 'FY_BY_REALTIME',
    'typoResult' : 'true',
    'salt'	: salt,
    'sign' : sign,
}



data = urllib.urlencode(data)
request = urllib2.Request(baseUrl,data=data,headers=headers)
response = urllib2.urlopen(request)
htmldata = response.read()
# dataJson = json.loads(htmls)
# tgt = dataJson['translateResult'][0][0]['tgt']

print gzip_uncompress(htmldata)

