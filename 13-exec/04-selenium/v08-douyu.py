'''
爬取斗鱼直播页内容
'''
from selenium import webdriver
import time
from lxml import etree


driver = webdriver.PhantomJS()

def get_page():
    driver.get('https://www.douyu.com/directory/all')
    time.sleep(5)
    html = driver.page_source
    return html

def parse(html):
    html = etree.HTML(html)
    lis = html.xpath('//ul[@id="live-list-contentbox"]/li')
    print(len(lis))
    for li in lis:
        title = li.xpath('./a/div/div/h3/text()')[0].strip()
        tag = li.xpath('./a/div/div/span/text()')[0].strip()
        author = li.xpath('./a/div/p/span[@class="dy-name ellipsis fl"]/text()')[0].strip()
        print(title,tag,author)



def main():
    html = get_page()
    parse(html)

if __name__ == '__main__':
    main()