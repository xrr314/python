'''
解析豆瓣音乐排行榜
https://music.douban.com/chart
'''


from selenium import webdriver
import os
from lxml import etree

# 路径
path = './v06/music_douban'
if not os.path.exists(path):
    os.makedirs(path)

driver = webdriver.PhantomJS()
driver.get('https://music.douban.com/chart')

driver.implicitly_wait(2)

file_name = path + "/1.png"
# driver.save_screenshot(file_name)
result = driver.page_source

html = etree.HTML(result)

ul_list = html.xpath('//ul[@class="col5"]')[0]
count = 0
for li in ul_list.xpath('.//li'):
    # print(li)
    index = li.xpath('./span[@class="green-num-box"]/text()')[0]
    # print(index)
    if(count<10):
        img = li.xpath('./a/img/@src')[0]
        # print(img)

        # 歌名
        name = li.xpath('.//h3/a/text()')
        if name:
            name = name[0]
            # print(name)

        # 歌手
        singer = li.xpath('.//p/text()')
        if singer:
            singer = singer[0]
            # print(singer)
    else:
        img = None
        name = li.xpath('.//p/a/text()')
        if name:
            name = name[0]
            # print(name)
        # 歌手
        singer = li.xpath('.//p/text()')
        if singer:
            singer = singer[1].replace('\n','').replace(' ','')
            # print(singer)
    count += 1
    print(index,img,name,singer)
