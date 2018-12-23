'''
爬取i包图网/视频
https://ibaotu.com/shipin/
视频抓取
'''
import requests
from lxml import etree

class Spider(object):
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        self.offset = 1

    def start(self,url):
        res = requests.get(url,headers=self.headers)
        html = etree.HTML(res.text)
        title = html.xpath('//a[@class="shade-box"]/span/text()')
        # print(title)
        src = html.xpath('//div[@class="video-play"]/video/@src')
        # print(src)
        # print(title,src)
        self.write_file(title,src)

    def write_file(self,file_name,file_src):
        for title,url in zip(file_name,file_src):
            rsp = requests.get('http:'+url,headers=self.headers)
            filename = str(title)+'.mp4'
            print(filename)
            with open('v12_video/'+filename,'wb') as f:
                f.write(rsp.content)


if __name__ == '__main__':
    spider = Spider()
    for i in range(1,11):
        url = 'https://ibaotu.com/shipin/7-0-0-0-0-{}.html'.format(str(i))
        spider.start(url)