'''
关于user_agent的请求头,最简单的反爬取通过user_agent来判断是否是机器人
使用Request方法可以添加headers信息,
然后再调用urlopen方法获取页面
--郎朗渔家(首页/来岛路线/常见问题)
http://www.langlang2017.com/index.html
http://www.langlang2017.com/route.html
http://www.langlang2017.com/FAQ.html
'''
from urllib import request
import random
def spider(url):
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    ]
    headers = {'User_Agent':random.choice(user_agent_list)}
    req = request.Request(url=url, headers = headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode('utf-8')
    # print(html)

    # 保存文件
    name = url.split('/')
    # print('name:{0}'.format(name))
    fileName = 'v02_'+name[-1]
    # print('filename:{0}'.format(filename))
    with open(fileName,'w',encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    url_list = [
        'http://www.langlang2017.com/index.html',
        'http://www.langlang2017.com/route.html',
        'http://www.langlang2017.com/FAQ.html'
    ]
    for url in url_list:
        spider(url)
        # print('* '*50)