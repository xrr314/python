from urllib import error, request, parse
from http import cookiejar
import json

#创建filecookiejar实例
filename='cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename=filename)
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
    #使用open 发起请求
    rsp=opener.open(req)
    #保存cookie
    #ignore_discard表示及时cookie将要被丢弃也会保存下来
    #ignore_expires表示文件中的cookie过期也会保存下来
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == '__main__':
    login()