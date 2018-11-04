'''
使用参数headers和params
研究返回结果
'''
import requests


url="http://www.baidu.com/s?"

kw={
    'wd':'王八蛋'
}
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
rsp=requests.get(url,params=kw,headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)