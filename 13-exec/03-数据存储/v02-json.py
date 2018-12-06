'''
爬取盗墓笔记,并保存数据
http://www.seputu.com/
'''

import requests,json
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

rsp = requests.get('http://www.seputu.com/', headers=headers)
# print(rsp.text)

soup = BeautifulSoup(rsp.text,'lxml')
content = []
for mulu in soup.find_all(class_="mulu"):
    # print(mulu)
    # 目录
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.text
        # print(h2_title)
    # 获取章节内容和url地址
    box = mulu.find(class_="box")
    # print(box)
    if box != None:
        list = []
        for a in box.find_all("a"):
            # print(a)
            href = a.get('href')
            box_title = a.get('title')
            # print(href,box_title)
            b = a.text
            # print(b)
            list.append({'href':href,'box_title':box_title})
        content.append({'title':h2_title,'content':list})


with open('gcd.json','a',encoding='utf-8') as f:
    json.dump(content,fp=f,indent=4,ensure_ascii=False)