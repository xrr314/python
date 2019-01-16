'''
获取豆瓣图书
https://book.douban.com/subject_search?search_text=python&cat=1001&start=0
'''

from selenium import webdriver
import time
from lxml import etree

i = 1
def spider(url):
    print('-----------开始第{}页爬取-----------'.format(i))
    driver = webdriver.PhantomJS()
    driver.get(url)
    # 等待
    time.sleep(2)
    driver.save_screenshot('./v04/open_{}.png'.format(str(i)))

    file_name = './v04/douban_dushu_open_{}.html'.format(str(i))
    with open(file_name,'w',encoding='utf-8') as f:
        f.write(driver.page_source)

    # 解析内容
    parse(file_name)
    driver.quit()
    print('-----------结束第{}页爬取-----------'.format(i))

# 解析数据
def parse(file):
    # 读取文件
    with open(file,'r',encoding='utf-8') as f:
        html = f.read()
        # print(html)
        html = etree.HTML(html)
        books = html.xpath('//div[@class="item-root"]')
        for book in books:
            # 封面图片链接
            book_src = book.xpath('./a/img/@src')[0]
            # 书名
            book_name = book.xpath('.//div[@class="title"]/a/text()')[0]
            # 书的链接
            book_url = book.xpath('.//div[@class="title"]/a/@href')[0]
            # 书的评分
            book_star = book.xpath('.//span[@class="rating_nums"]/text()')[0]
            # 作者
            book_author = book.xpath('.//div[@class="meta abstract"]/text()')[0].split('/')[1].strip()


            print(book_src,book_name,book_url,book_star,book_author)




if __name__ == '__main__':
    for i in range(5):
        url = 'https://book.douban.com/subject_search?search_text=python&cat=1001&start={}'.format(str(i*15))
        spider(url)