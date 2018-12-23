'''

优化页面获取,直接通过检测页面中红下一页按钮的url获取下一页的地址,实现自动的爬取

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

        # 处理下一页
        next_page = html.xpath('//a[@class="next"]/@href')
        if next_page:
            next_page = 'http:' + html.xpath('//a[@class="next"]/@href')[0]
        else:
            return

        self.write_file(title,src)
        self.start(next_page)

    def write_file(self,file_name,file_src):
        for title,url in zip(file_name,file_src):
            rsp = requests.get('http:'+url,headers=self.headers)
            filename = str(title)+'.mp4'
            print(filename)
            with open('v12_video/'+filename.replace('/','_'),'wb') as f:
                f.write(rsp.content)


if __name__ == '__main__':
    spider = Spider()
    url = 'https://ibaotu.com/shipin/7-0-0-0-0-{}.html'.format(str(1))
    spider.start(url)