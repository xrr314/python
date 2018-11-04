'''
使用urllib.request请求,并把内容打印出来
'''
from urllib import request

if __name__ == '__main__':
    url='https://jobs.zhaopin.com/700497024250013.htm'
    #打开相应的url并把相应的页面作为返回
    #urlopen返回的结果为文件形式,无法直接读取需要进行转码
    rsp=request.urlopen(url)
    #读取返回结果
    #读取出来的内容为bytes内容,不利于阅读
    html=rsp.read()

    #想要把bytes内容进行转换成字符串,需要解码
    html=html.decode()


    print(html)