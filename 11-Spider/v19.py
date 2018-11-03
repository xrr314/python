'''

    通过查找,能够找到salt的构造方式
        r=""+((new Date).getTime() + parseInt(10 * Math.random(), 10));
    sign就是一个MD5的值
        sign: n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK")
'''

'''
    var r = function(e) {
        var t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
        return {
            salt: t,
            sign: n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK")
        }
    };
'''
import time,random

def getSalt():
    '''
    salt公式
    :return:
    '''
    salt=int(time.time()*1000)+random.randint(0,10)
    return salt;

def getMD5(v):
    import hashlib
    md5=hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign=md5.hexdigest()
    return sign

#sign=n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK")
def getSign(key,salt):
    sign='fanyideskweb'+key+salt+'6x(ZHw]mwzX#u0V7@yfwK'
    sign=getMD5(sign)
    return sign

from urllib import request,parse

def youdao(key):

    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    salt=str(getSalt())
    data={
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": getSign(key,salt),
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
        "Content-Length":len(data),
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