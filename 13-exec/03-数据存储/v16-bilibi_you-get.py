'''
爬取bilibili视频,通过you-get下载
you-get
    https://www.cnblogs.com/ys-wuhan/p/6057526.html
    能够自动检索页面中的视频/音频/图像,下载和解析页面


https://search.bilibili.com/all?keyword=%E8%A7%86%E9%A2%91&from_source=banner_search
通过控制台,查看json类型请求
https://api.bilibili.com/x/web-interface/search/all?jsonp=jsonp&highlight=1&keyword=视频&from_source=banner_search&single_column=0&callback=__jp0
去除末尾访问
https://api.bilibili.com/x/web-interface/search/all?jsonp=jsonp&highlight=1&keyword=视频&from_source=banner_search&single_column=0
https://api.bilibili.com/x/web-interface/search/all?jsonp=jsonp&highlight=1&keyword=%E8%A7%86%E9%A2%91&from_source=banner_search&single_column=0

'''

import requests
import json
import os


# 获取srcurl地址/title
def get_info(startPage,endPage):
    data = []
    for page in range(startPage,endPage):
        url = 'https://api.bilibili.com/x/web-interface/search/all?jsonp=jsonp&highlight=1&keyword=%E8%A7%86%E9%A2%91&from_source=banner_search&single_column={}'.format(page)
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
        decodejson = requests.get(url,headers=headers).text
        decodejson = json.loads(decodejson)
        # print(decodejson)
        items = decodejson['data']['result']['video']
        for item in items:
            # print(item)
            title = item['title']
            video_url = item['arcurl']
            # print(title,video_url)
            data.append([title,video_url])
    # print(data)
    return data

def downloadVideo(data):
    path = './v16-video/'
    if not os.path.exists(path):
        os.makedirs(path)
    for title,url in data:
        root = path + title.replace('/','')
        print('正在下载{}'.format(title))
        # 利用os.system来操作you-get下载视频
        os.system("you-get -o {} {}".format(root,url))
        print('视频:{}...下载完成'.format(title))


if __name__ == '__main__':
    data = get_info(1,2)
    downloadVideo(data)