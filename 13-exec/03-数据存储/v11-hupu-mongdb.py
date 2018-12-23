'''
爬取虎扑NBA模块内容,使用mongdb存储
https://bbs.hupu.com/nba
'''
import requests
from lxml import etree
from v00_mongdb import MongoAPI

def spider(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    # print(res.text)
    html = etree.HTML(res.text)
    return html

def parse(html):
    # 通过这个方式获取我们发现title数量会少于href的数量,
    # 通过html页面查看发现部分title是存放在<b>标签中,
    # 我们这里可以通过href的请求地址来获取对应的标题
    # titles = html.xpath('//form/div/ul/li/div[@class="titlelink box"]/a/text()')
    # print(titles)
    hrefs = html.xpath('//form/div/ul/li/div[@class="titlelink box"]/a[@class="truetit"]/@href')
    # print(len(hrefs))
    # 拼接出完整的url地址
    titles = []
    hrefs = ['http://bbs.hupu.com'+i for i in hrefs]
    # print(hrefs)
    for href in hrefs:
        print(href)
        data = spider(href)
        title = data.xpath('//div[@class="bbs-hd-h1"]/h1/text()')[0]
        # print(title)
        titles.append(title)
    # print(titles)
    authors = html.xpath('//form/div/ul/li/div[@class="author box"]/a[@class="aulink"]/text()')
    # print(authors)
    times = html.xpath('//form/div/ul/li/div[@class="author box"]/a[2]/text()')
    # print(times)
    datas = html.xpath('//form/div/ul/li/span/text()')
    datas = [x.split('\xa0/\xa0') for x in datas]
    # print(datas)
    # 回复数
    replies = [x[0] for x in datas]
    # print(replies)
    # 浏览数
    browses = [x[1] for x in datas]
    # print(browses)
    last_times = html.xpath('//form/div/ul/li/div[3]/a/text()')
    # print(last_times)
    last_names = html.xpath('//form/div/ul/li/div[3]/span/text()')
    # print(last_names)
    # print(len(titles),titles)
    # print(len(hrefs),hrefs)
    # print(len(authors),authors)
    # print(len(times),times)
    # print(len(replies),replies)
    # print(len(browses),browses)
    # print(len(last_times),last_times)
    # print(len(last_names),last_names)

    # zip使用查看v10-list_change.py
    items = zip(titles,hrefs,authors,times,replies,browses,last_times,last_names)
    # print(items)
    return items


def data_storage(items):
    hupu_post = MongoAPI('127.0.0.1',27017,'hupu','nba')
    # titles, hrefs, authors, times, replies, browses, last_times, last_names
    for item in items:
        hupu_post.add({
            "titles": item[0],
            "hrefs": item[1],
            "authors": item[2],
            "times": item[3],
            "replies": item[4],
            "browses": item[5],
            "last_times": item[6],
            "last_names": item[7]
        })
        # print('数据存储完成')


def main():
    for i in range(1,11):
        url = 'https://bbs.hupu.com/nba-{0}'.format(str(i))
        # print(url)
        print('开始扫描第{}页,请稍等...'.format(i))
        html = spider(url)
        items = parse(html)
        data_storage(items)
        print('完成第{}页内容存储'.format(i))





if __name__ == '__main__':
    main()