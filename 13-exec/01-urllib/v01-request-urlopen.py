'''
简单回顾一下
urlopen发起请求,返回页面内容
'''
# from urllib import request
#
# url = 'http://www.w3school.com.cn/json/index.asp'
# rsp = request.urlopen(url)
#
# print('rsp:{0}'.format(rsp))
#
# content = rsp.read().decode('utf-8')
# print('content:{0}'.format(content))

'''
w3c简单练习
url = 'http://www.w3school.com.cn/json/index.asp'
decode()方法中的参数,可以通过观察页面的html信息头meta标签查看,如果不填默认utf-8
method:get
'''

from  urllib import request

rsp = request.urlopen('http://www.w3school.com.cn/json/index.asp')

content = rsp.read().decode('gb2312')
print(content)

