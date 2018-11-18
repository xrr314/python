'''
要求导入scrapy
所有的类一般是XXXSpider命名
所有的爬虫类是scrapy.Spider的子类
'''

import scrapy

class BaiduSpider(scrapy.Spider):

    # name是爬虫的名字
    name = 'baidu'

    # 定义起始URL列表
    start_urls=['http://www.baidu.com']

    # 负责分析Downloader下载得到的结果
    # 就是重写scrapy.Spider中的parse方法
    def parse(self, response):
        '''
        我们这保存网页即可
        :param response:
        :return:
        '''
        with open('baidu.html','w',encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))