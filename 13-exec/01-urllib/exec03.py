''''
有道翻译
同样是采用的post请求方式
观察请求时的form data
    在这中间变化的只有i,salt,sign
    i 我们输入的内容
    salt 时间戳(精确的ms),可以通过time.time()获得当前的时间的秒*1000得到
    sign 肯定是通过js变化得到
        通过浏览器的F12中的网络-JS查看页面加载的JS,查询里面含有salt的内容,查到fanyi.min.js
        通过CTRL+F查找salt我们可以查找到
            define("newweb/common/service", ["./utils", "./md5", "./jquery-1.7"], function(e, t)
        的方法,
            var t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
        其中的salt = t ,和我们猜想的时间戳+加上一个0-10的整数
        这里我们可以确定
            salt = int(time.time()*1000)+random.randint(0,10)
        而sign= n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r"
        这是MD5的一个加密,其中前面和后面的内容为固定的字符串,中间为e,t
        t,我们这里已经知道就是salt,而e我们继续往下看
            i: e.i,
        我们猜测e就是我们输入的单词
'''
'''
搜索boy时显示的form data
i: boy
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 1543322425748
sign: 48b18f94f4ad4ad539add8a560765c75
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTIME
typoResult: false
'''
'''
hello时的form data
i: hello
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 1543322602555
sign: bb1f661cfd5dae3656708f2422795187
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTIME
typoResult: false
'''
'''
define("newweb/common/service", ["./utils", "./md5", "./jquery-1.7"], function(e, t) {
    var n = e("./jquery-1.7");
    e("./utils");
    e("./md5");
    var r = function(e) {
        var t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
        return {
            salt: t,
            sign: n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")
        }
    };
    t.recordUpdate = function(e) {
        var t = e.i
          , i = r(t);
        n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/bettertranslation",
            data: {
                i: e.i,
                client: "fanyideskweb",
                salt: i.salt,
                sign: i.sign,
                tgt: e.tgt,
                modifiedTgt: e.modifiedTgt,
                from: e.from,
                to: e.to
            },
            success: function(e) {},
            error: function(e) {}
        })
    }
    ,
    t.recordMoreResultLog_get = function(e) {
        n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/ctlog",
            data: {
                i: e.i,
                action: "GET_MORE_TRANSLATION",
                from: e.from,
                to: e.to
            },
            success: function(e) {},
            error: function(e) {}
        })
    }
    ,
    t.recordMoreResultLog_choose = function(e) {
        n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/ctlog",
            data: {
                i: e.i,
                tgt: e.tgt,
                systemName: e.systemName,
                pos: e.pos,
                action: "SELECT_OTHER_TRANSLATION",
                from: e.from,
                to: e.to
            },
            success: function(e) {},
            error: function(e) {}
        })
    }
    ,
    t.generateSaltSign = r
}),
'''
from urllib import request,parse
import time
import random
import hashlib
import json

def getMD5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value,encoding='utf-8'))
    sign = md5.hexdigest()
    return sign

def parse_json(content):
    data_json = json.loads(content)
    sr_dict = data_json['smartResult']
    items = sr_dict['entries']
    # print(items)
    for item in items:
        print(item)

def yd_fanyi(key):
    base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    salt = int(time.time()*1000)+random.randint(0,10)
    sign = "fanyideskweb" + key + str(salt) +"sr_3(QOHT)L2dx#uuGR@r"
    sign = getMD5(sign)
    data = {
        'i':key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'

    }
    data = parse.urlencode(data)

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding":"gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=165480017@218.107.205.181; JSESSIONID=abcNK0zpWsk928EIzykBw; OUTFOX_SEARCH_USER_ID_NCOO=435780751.646305; ___rl__test__cookies=1540993772505",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"

    }
    req = request.Request(base_url,data=bytes(data,encoding='utf-8'),headers=headers)
    rsp = request.urlopen(req)
    content = rsp.read().decode()
    # print(content)
    parse_json(content)


if __name__ == '__main__':
    while 1:
        key = input('请输入你要翻译的内容:')
        if key == 'q':
            break
        yd_fanyi(key)