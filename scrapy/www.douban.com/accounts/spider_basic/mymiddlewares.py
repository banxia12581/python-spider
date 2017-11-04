#coding:utf8
from settings import USER_AGENS,PROXIES
import random
import base64

# 随机更换浏览器身份中间件
class RandomUserAgent(object):
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENS)
        request.headers.setdefault('User-Agent',user_agent)

# 随机更换代理ip
class RandomProxy(object):
    def process_request(self,request , spider):
        proxy = random.choice(PROXIES) # 随机选出一个代理
        if proxy.get('auth') is None: # 免费代理
            request.meta['proxy'] = 'http://' + proxy['host']

        else : # 收费代理
            auth = base64.b64encode(proxy['auth'])
            request.headers['Proxy-Authorization'] = 'Basic ' + auth
            request.meta['proxy'] = 'http://' + proxy['host']