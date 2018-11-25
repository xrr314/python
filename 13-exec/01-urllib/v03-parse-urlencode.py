'''
转码
urllib.parse.quote('中文')
解码
parse.unquote('xxxxxxxxxxxxxx')
使用urllib.parse.urlencode()
    实现get请求时的条件拼接
https://tieba.baidu.com/f?kw=%E5%A3%B0%E6%8E%A7&ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=%E5%A3%B0%E6%8E%A7&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=%E5%A3%B0%E6%8E%A7&ie=utf-8&pn=100
'''
from urllib import request,parse


base_url = 'https://tieba.baidu.com/f?'
name = input('请输入名称')
page = input('请输入页码')

for i in range(int(page)):
# i = int(page)
    qs = {
        'kw':name,
        'pn':i*50
    }
    qs_data = parse.urlencode(qs)
    url = base_url + qs_data
    # print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

    req = request.Request(url,headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    # print(html)
    fileName = 'v03_'+name+'_'+str(i+1)+'.html'
    with open(fileName,'w',encoding='utf-8') as f:
        f.write(html)