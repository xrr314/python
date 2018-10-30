from urllib import error, request, parse
from http import cookiejar
import json

#创建cookiejar实例
cookie = cookiejar.CookieJar()
#生成cookie的管理器
cookie_handler=request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handle=request.HTTPHandler()

#生成https管理器
https_handler=request.HTTPSHandler()


#创建请求管理器
opener=request.build_opener(http_handle,https_handler,cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名密码,
    :return:
    '''
    url = 'http://www.renren.com/PLogin.do'
    #此键值对需要登录form的两个对应的input中提取name
    data = {"email" : "15080334894",
          "password" : "xrr940314"
          }
    data=parse.urlencode(data).encode()
    req=request.Request(url,data=data)
    rsp=opener.open(req)


def getHomePage():
    url='http://www.renren.com/968526175/profile'
    #如果已经执行了login函数,则opener自动已经包含了相应的cookie
    rsp=opener.open(url)
    html=rsp.read().decode()
    with open('rsp1.html','w') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()