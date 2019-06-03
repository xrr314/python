from DataOutput import DataOuput
from HtmlParse import HtmlParse
from HtmlDownload import HtmlDownload
from UrlManager import UrlManager


class SpiderMan(object):
    def __init__(self):
        self.manger = UrlManager()
        self.download = HtmlDownload()
        self.parse = HtmlParse()
        self.outpu = DataOuput()

    def crawl(self,root_url):
        '''
        添加入口url
        :param root_url:
        :return:
        '''
        self.manger.add_new_url(root_url)
        # 判断url管理器中是否有新的url地址,同时判断抓取了多少个url
        while(self.manger.has_new_url() and self.manger.old_url_size()<100):
            try:
                # 从URL管理器中获取新的URL地址
                new_url = self.manger.get_new_url()
                # html下载器进行页面下载
                html = self.download.download(new_url)
                # html解析获取数据
                new_urls,data = self.parse.parse(new_url,html)
                # 将获取到的url地址添加到url管理器中
                self.manger.add_new_urls(new_urls)
                # 数据存储
                self.outpu.store_data(data)
                self.outpu.ouput_html()
                print('已抓取%s个链接'%self.manger.old_url_size())
            except Exception as e:
                print('crawl fail',e)

if __name__ == '__main__':
    spider_man = SpiderMan()
    url = 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
    spider_man.crawl(url)