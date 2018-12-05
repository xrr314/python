'''
博客园
www.cnblogs.com

'''
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'cache-control':'max-age=0'
}
html = requests.get('https://www.cnblogs.com/cate/python/',headers = headers)
# print(html.text)
# 使用lxml解析页面
soup = BeautifulSoup(html.text,'lxml')
# 不同与我们直接写xpath,而是使用选择器
# 返回一个列表
items = soup.select('div[class="post_item_body"]')
# print(items)

for item in items:
    # 标题
    title = item.select('h3 a[class="titlelnk"]')[0].get_text()
    # 详情链接,类似于字典的取值方式
    href = item.select('h3 a[class="titlelnk"]')[0].get('href')
    # href = item.select('h3 a[class="titlelnk"]')[0]['href']
    # 作者
    author = item.select('div[class="post_item_foot"] a')[0].get_text()
    # 作家的主页链接
    author_home = item.select('div[class="post_item_foot"] a')[0].get('href')
    # 简介(并去除没用的换行和空格)
    info = item.select('p[class="post_item_summary"]')[0].get_text().strip('\n').strip(' ').strip('\r\n')

    datas = item.select('div[class="post_item_foot"]')[0].get_text()
    # print(datas)
    datas = datas.split(' ')
    # 发布时间
    time = datas[6]+" "+datas[7]
    # 评论信息数(采用切割和分割的办法获取同一个字符串中有用的信息)
    pinglun = datas[-1].lstrip('评论(').split(')')[0]
    # 阅读数
    yuedu = datas[-1].rstrip(')').split('(')[-1]

