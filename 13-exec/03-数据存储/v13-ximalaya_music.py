'''
喜马拉雅音乐下载
https://www.ximalaya.com/


pypinyin一个新包,实现讲中文转成拼音
    lazy_pinyin:不含声调
    pinyin:含有声调

'''


from pypinyin import lazy_pinyin
import requests
import re
import json
from urllib import request
import time

def start_spider(str,headers):
    url = 'https://www.ximalaya.com/yinyue/{}'.format(str)
    html = requests.get(url,headers=headers).text
    return html

# 翻译歌曲类型
def fanyi(num):
    var = lazy_pinyin(num)
    str = ''.join(var)
    return  str


# 获取albumId值
def get_albumId(html):
    albumIds = re.findall(r'"albumId":(.*?),',html)
    # print(albumIds)
    albumId = albumIds[0]
    # for albumId in albumIds:
    # print(albumId)
    time.sleep(1)
    # 构建下载地址
    down_url = 'https://www.ximalaya.com/revision/play/album?albumId={}&sort=-1&pageSize=30&pageNum=1'.format(albumId)
    print(down_url)
    # 请求音乐json文件
    music_json = requests.get(down_url,headers=headers).text
    # print(music_json.status_code,music_json.text)
    return music_json

# 开始下载音乐
def download_music(music_json):
    # music_json为str需要转成字典格式
    # print(type(music_json))
    print(music_json)
    music_json = json.loads(music_json)
    # print(type(music_json))
    # 获取标题和下载链接
    songInfo = music_json['data']['tracksAudioPlay']
    titles = []
    for song in songInfo:
        title = song['trackName'].replace('/','-')
        titles.append(title)
        # print(title)
        try:
            print('正在下载--{}'.format(title))
            request.urlretrieve(song['src'],'./v13_music/'+title+'.m4a')
            print('下载完成--{}'.format(title))
        except:
            print('下载失败~~{}'.format(title))
    print('下载结束')

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host':'www.ximalaya.com',

    }


if __name__ == '__main__':
    music_type = input('please input your music type:')
    str = fanyi(music_type)
    html = start_spider(str,headers)
    music_json = get_albumId(html)
    download_music(music_json)