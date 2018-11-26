from urllib import request,parse
import json

def baidufanyi(kw):
    url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw' :kw
    }

    data = parse.urlencode(data)
    headers = {
        'Content-Length':len(data),
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    req = request.Request(url= url,headers=headers,data=bytes(data,encoding='utf-8'))
    rsp = request.urlopen(req)
    html=rsp.read().decode()
    # print(html)
    json_data = json.loads(html)
    # print(json_data)
    for item in json_data['data']:
        print(item['k']+'--'+item['v'])

if __name__ == '__main__':
    kw = input('请输入你要翻译的内容:')
    baidufanyi(kw)