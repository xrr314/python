'''

利用request下载页面
自动检测页面编码

'''
from urllib import request,parse
'''
掌握url进行参数编码
使用prase
'''
if __name__ == '__main__':
    url='http://www.baidu.com/s?'
    wd=input("input your keyword:")

    qs = {
        "wd": wd
    }
    # 转换url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # 如果直接用可读的带参数的url，是不能访问的
    # fullurl = 'http://www.baidu.com/s?wd=大熊猫'

    rsp = request.urlopen(fullurl)

    html = rsp.read()

    # 使用get取值保证不会出错
    html = html.decode()
    print(html)
