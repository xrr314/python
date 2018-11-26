'''
cookie防止页面的登录检查
添加cookie
通过http.cookiejar.CookieJar来创建一个cookie对象
使用request.HTTPCookieProcessor创建cookie处理器
通过request.build_opener()获得opener对象

方式1:
通过opener.open(url)得到页面
方式2:
把生成opener使用,request.install_opener()来为全局加载cookie
'''
'''
登录华为官网
使用方式post
分析登录地址
url = 'https://www.huawei.com/en/accounts/LoginPost'
查看头部信息
userName: xrr19940314@163.com
pwd: qgwYFZmowINWdDsCtmtgLOYYng3HF2oSbX1oeClCcSwRO33dcoMGub8UaL4DnMRyt+KS/KNAwiWe9QcSnwFNSe/YzB65UCjOwLYymNvmCxNKbDvNvMYHfhsQKhJuYsQhaXfYbztycq/7SMVtpdy5rXEapkAcflOL+YUvgyebX18=
languages: zh
fromsite: www.huawei.com
authMethod: password
'''

from urllib import request,parse
from  http import cookiejar
import random

#生成cookie对象
cookie = cookiejar.CookieJar()
#生辰cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#生成http管理器
http_handler = request.HTTPHandler()
#生成https管理器
https_handler = request.HTTPSHandler()

#发起请求管理器
opener = request.build_opener(cookie_handler,http_handler,https_handler)


# 构建登录函数
def login(url):
    data = {
        'userName': 'xrr19940314@163.com',
        'pwd':'xrr940314',
        'languages': 'zh',
        'fromsite': 'www.huawei.com',
        'authMethod': 'password'
    }
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    ]
    headers = {'User_Agent': random.choice(user_agent_list)}
    data = parse.urlencode(data)
    req = request.Request(url = url, data = bytes(data, "utf-8"), headers=headers)
    rsp = opener.open(req)
    print(rsp.read().decode())

if __name__ == '__main__':
    url = 'https://www.huawei.com/en/accounts/LoginPost'
    login(url)
