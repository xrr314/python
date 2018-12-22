'''
酷狗音乐top500抓取
https://www.kugou.com/yy/rank/home/1-8888.html?from=rank
我们要爬取top500的所有歌曲信息,但是页面只显示了1-22的数据
我们尝试修改地址的1-8888.html
我们可以通过访问2-8888.html获得23-44的歌曲信息
我们可以尝试23-8888.html能够获取到所有的500收歌曲信息
'''

import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

def kg_spider(url):
    '''
    获取酷狗音乐top500,保存到mongdb
    :param url: 请求地址
    :return:
    '''
    res = requests.get(url,headers=headers)
    # print(res.text)
    soup = BeautifulSoup(res.text,'lxml')
    ranks = soup.select('.pc_temp_num')
    titles = soup.select('.pc_temp_songlist  > ul > li > a')
    times = soup.select('.pc_temp_time')
    for rank,title,time in zip(ranks,titles,times):
        rank = rank.get_text().strip()
        # print(rank)
        song = title.get_text().split(' - ')[-1]
        # print(song)
        singer = title.get_text().split(' - ')[0]
        # print(singer)
        song_time = time.get_text().strip()
        # print(song_time)
        print(rank,song,singer,song_time)
        data = {
            'rank':rank,
            'song':song,
            'singer':singer,
            'song_time':song_time
        }
        storage_mongdb(data)
        print("---"*20)


# mongdb数据存储
def storage_mongdb(data):
    client = MongoClient()
    songs = client.KG_DB.songs
    song_id = songs.insert(data)
    print(song_id)
'''
如何获取音乐的下载地址
通过点击页面的中的播放,可以能够进行页面跳转
在控制台中选中media来捕捉歌曲的实际地址
http://fs.w.kugou.com/201812221245/1095a6190c2feb9f540b79f1cbb39495/G111/M06/1D/10/D4cBAFoL9VyASCmXADTAFw14uaI428.mp3
'''
if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{0}-8888.html?from=rank'.format(str(i)) for i in range(1,24)]
    for url in urls:
        data = kg_spider(url)
        time.sleep(1)