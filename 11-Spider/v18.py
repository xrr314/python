'''

    破解有道翻译

'''
from urllib import request,parse

def youdao(key):

    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data={
        "i": "girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1540993772511",
        "sign": "a8431edc68b061fdc5d69e0a93e0fa26",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    data=parse.urlencode(data).encode()

    headers={
        "Accept":"application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Content-Length":"200",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie":"DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=165480017@218.107.205.181; JSESSIONID=abcNK0zpWsk928EIzykBw; OUTFOX_SEARCH_USER_ID_NCOO=435780751.646305; ___rl__test__cookies=1540993772505",
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"

    }
    req=request.Request(url,headers=headers,data=data)
    rsp=request.urlopen(req)
    html=rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao('boy')