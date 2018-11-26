'''
判断代理是否可用
'''
from urllib import request
import random

# 有代理
proxy_list = [
    {'http':'47.97.112.249:80'},
    {'https':'123.7.61.8:53281'},
    {'http':'58.53.128.83:3128'}
]
proxy = random.choice(proxy_list)
proxy_handler = request.ProxyHandler(proxy)
# 无代理
proxy_none = request.ProxyHandler()


user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    ]
headers = {'User_Agent':random.choice(user_agent_list)}

opener  = request.build_opener(proxy_none)
url = 'http://www.langlang2017.com'
req = request.Request(url=url,headers=headers)

isProxy = input('是否使用代理:')
if isProxy == "1" :
    opener = request.build_opener(proxy_handler)

rsp = opener.open(req)

print(rsp.read().decode())
