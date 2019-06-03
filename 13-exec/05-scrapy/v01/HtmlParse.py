'''
解析器
'''

import re
from bs4 import BeautifulSoup
from urllib import request


class HtmlParse(object):
    def parse(self,page_url,html_cont):
        '''
        解析页面内容,抽取URL和数据
        :param page_url: 下面页面的url地址
        :param html_cont: 下载页面的内容
        :return:
        '''
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'lxml',from_encoding='utf-8')
        new_url = self._get_new_url(page_url,soup)
        new_data = self._get_new_data(page_url, soup)
        return new_url,new_data

    def _get_new_url(self,page_url,soup):
        '''
        爬取新的URL地址
        :param page_url:
        :param soup:
        :return:
        '''
        new_urls = set()
        # 抓取符合要求的a标记
        links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))

        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼接完整URL地址
            new_full_url = request.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        '''
        抓取有效数据
        :param page_url:
        :param soup:
        :return:
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title
        summary = soup.find('div',class_="lemma-summary")
        data['summary'] = summary.get_text()

        return data
