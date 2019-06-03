'''
变量:
    - 已经抓取的URL集合
    - 未抓取的URL集合
1.是否有带取的URL地址   has_new_url()
2.添加新的URL到为爬去的集合中   add_new_url()   add_new_urls(urls)
3.获取一个url地址     get_new_url()
4.获取未爬取URL集合的大小     new_URL_size()
5.获取已爬取URL集合的大小     old_url_size()
'''

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()   # 未爬取的URL集合
        self.old_urls = set()   # 已经爬取的URL地址

    def has_new_url(self):
        '''
        判断是否有为爬取的url
        :return:
        '''
        return self.new_url_size()!=0

    def get_new_url(self):
        '''
        获取一个未抓取的url
        :return:
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        '''
        爬取的url大小
        :return:
        '''
        return len(self.new_urls)

    def old_url_size(self):
        '''
        未爬取的url大小
        :return:
        '''
        return len(self.old_urls)