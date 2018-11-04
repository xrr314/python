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



if __name__ == '__main__':
    '''
        执行完之后,会得到cookie
    '''
    login()
    print(cookie)
    for item in cookie:
        # print(type(item))
        print(item)
        # for i in item:
        #     print(i)