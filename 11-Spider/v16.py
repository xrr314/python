from urllib import error, request, parse
from http import cookiejar
import json
'''
    读取cookie保存的文件,然后访问网页
    运行是注意cookie放在过期的情况,之后运行前需要想运行v15来获取最新的cookie
'''
#创建filecookiejar实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)

#生成cookie的管理器
cookie_handler=request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handle=request.HTTPHandler()

#生成https管理器
https_handler=request.HTTPSHandler()


#创建请求管理器
opener=request.build_opener(http_handle,https_handler,cookie_handler)

def getHomePage():
    url='http://www.renren.com/968526175/profile'
    #如果已经执行了login函数,则opener自动已经包含了相应的cookie
    rsp=opener.open(url)
    html=rsp.read().decode()
    with open('rsp1.html','w') as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()