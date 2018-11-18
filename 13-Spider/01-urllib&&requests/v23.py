import requests,json
from urllib import parse

if __name__ == '__main__':
    url='https://fanyi.baidu.com/sug'

    data = {
        # girl是翻译输入的英文内容，应该是由用户输入，此处使用硬编码
        'kw': 'girl'
    }

    headers={
        'Content-Length':str(len(data))
    }

    rsp=requests.post(url,data=data,headers=headers)

    print(rsp.json())

