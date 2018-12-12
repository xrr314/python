'''
爬取网易云歌手信息
music.163.com
话语男歌手
https://music.163.com/discover/artist/cat?id=1001&initial=-1
https://music.163.com/discover/artist/cat?id=1001&initial=65

其他男歌手
热门:https://music.163.com/discover/artist/cat?id=4001&initial=-1
A:https://music.163.com/discover/artist/cat?id=4001&initial=65
B:https://music.163.com/discover/artist/cat?id=4001&initial=66
C:https://music.163.com/discover/artist/cat?id=4001&initial=67
...
其他:https://music.163.com/discover/artist/cat?id=1001&initial=0
'''
import requests
from bs4 import BeautifulSoup
import csv
import random


# print(init_list)
User_Agent_list=[
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
]

def get_singers(url):
    headers = {
        'User-Agent':random.choice(User_Agent_list),
        'Host':'music.163.com',
        'Referer':'https://music.163.com/'
    }
    rsp = requests.get(url,headers=headers)
    soup = BeautifulSoup(rsp.text,'lxml')
    for item in soup.find_all('a',attrs={'class':'nm nm-icn f-thide s-fc0'}):
        artist_name = item.string
        artist_id = item['href'].replace('/artist?id=','').strip()
        print(artist_id,artist_name)
        try:
            writer.writerow((artist_id,artist_name))
        except Exception as e:
            print(e,'写入失败~~~')



if __name__ == '__main__':
    id_list = [1001, 1002, 1003, 2001, 2002, 2003, 6001.6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]
    init_list = [-1, 0]
    a = [x for x in range(65, 91)]
    for a1 in a:
        init_list.append(a1)
    base_url = 'https://music.163.com/discover/artist/cat?id='

    # 文件存储位置
    csvfile = open('v09_music_163.csv','a')
    writer = csv.writer(csvfile)
    writer.writerow(('artist_id','artist_name'))

    for id in id_list:
        url1 = base_url+str(id)+'&initial='
        for init1 in init_list:
            url = url1+str(init1)
            get_singers(url)