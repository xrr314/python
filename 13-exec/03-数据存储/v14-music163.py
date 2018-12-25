'''
网易云音乐爬取
http://m10.music.126.net/20181225201029/1c76052a560dffb60949db9803e00853/ymusic/025f/510c/025d/5573c16cc6ffb6b67266576904e4db63.mp3


'''

from tkinter import *
import requests
from urllib import request
from bs4 import BeautifulSoup
import os

'''
音乐下载外链
http://music.163.com/song/media/outer/url?id=

1.获取页面源码
https://music.163.com/#/playlist?id=924680166
2.获取歌曲id和名称
3.下载音乐
'''

def music_spider():
    # 获取TK中输入ur
    url = entry.get()
    # url = 'https://music.163.com/playlist?id=924680166'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host':'music.163.com',
        'Referer':'https://music.163.com/'
    }
    # 请求页面详情
    res = requests.get(url,headers=headers)
    # print(res.text)
    soup = BeautifulSoup(res.text,'lxml')
    music_dict={}
    items = soup.find('ul',{'class':'f-hide'}).find_all('a')
    # print(items)
    for item in items:
        music_id = item.get('href').strip('/song?id=')
        music_name = item.text.replace('/','_')
        # print(music_id,music_name)
        music_dict[music_id] = music_name

    # print(music_dict)
    for song_id in music_dict:
        # 拼接下载地址
        song_url = 'http://music.163.com/song/media/outer/url?id='+str(song_id)+'.mp3'
        print(song_url)
        # 设置下载路径
        path = './v14_music163/'
        if not os.path.exists(path):
            os.mkdir(path)

        # 添加数据到控件中
        text.insert(END,'正在下载--{}'.format(music_dict[song_id]))
        # 文本狂向下滚动
        text.see(END)
        # 更新
        text.update()
        # 禁止重定向allow_redirects=False
        res = requests.get(song_url,headers=headers,allow_redirects=False)
        # print(res.status_code)
        # 在请求头中包含真实的下载地址
        # print(res.headers)
        dict = res.headers
        down_url = dict['Location']
        # print(down_url)
        request.urlretrieve(down_url,path+music_dict[song_id]+'.mp3')
    text.insert(END,'下载完成')


# 创建窗口
root = Tk()

# 设置窗口标题
root.title('网易云音乐下载器')
# 设置窗口大小
root.geometry('850x550')
# 窗口定位
root.geometry('+200+150')
# 设置下载器标签,请输入下载地址
label = Label(root,text="请输入下载地址",font=('仿宋',15))
# 定位pack palce grid
label.grid()

# 输入框
entry = Entry(root,font=('仿宋',20),width=48)
entry.grid(row=0,column=1)

# 设置列表框
text = Listbox(root,font=('仿宋,10'),width=80,height=24)
text.grid(row=1,columnspan=2)

# 开始按钮
button1 = Button(root,text="Start",font=('仿宋',15),command=music_spider)
button1.grid(row=2,column=0,sticky='w')
# 退出按钮
button2 = Button(root,text="Qiut",font=('仿宋',15),command=root.quit)
button2.grid(row=2,column=1,sticky='e')

# 显示窗口
root.mainloop()