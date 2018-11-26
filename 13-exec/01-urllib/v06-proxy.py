'''
隐藏真实的IP
使用列表存放proxy地址
通过request.ProxyHandler(proxy)创建代理处理器
通过request.build_opener(xxx)创建opener对象
之后处理方式同cookie
方式1:
通过opener.open(url)得到页面
方式2:
把生成opener使用,request.install_opener()来为全局加载proxy
'''
from urllib import request
import random

# 代理
proxy_list = [
    {'http':'47.97.112.249:80'},
    {'https':'123.7.61.8:53281'},
    {'http':'58.53.128.83:3128'}
]

proxy = random.choice(proxy_list)
proxy_handler = request.ProxyHandler(proxy)
opener = request.build_opener(proxy_handler)
# request.install_opener(opener)
url = 'http://www.langlang2017.com'

user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    ]
headers = {'User_Agent':random.choice(user_agent_list)}

req = request.Request(url,headers=headers)

rsp = opener.open(req)

print(rsp.read().decode())