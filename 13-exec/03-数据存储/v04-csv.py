'''

'''
import requests,csv
from lxml import etree
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

rsp = requests.get('http://www.seputu.com/', headers=headers)

html = etree.HTML(rsp.text)

div_mulus = html.xpath('//*[@class="mulu"]')

rows = []
for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('.//h2/text()')
    # print(div_h2)
    if len(div_h2)>0:
        h2_title = div_h2[0]
        # print(h2)
    a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
    for a in a_s:
        href = a.xpath('./@href')[0]
        box_title = a.xpath('./@title')[0]
        # print(href,box_title)
        # 对box_title内的内容进行处理
        # 方式1:自己想到的办法
        # box_title = box_title.split(' ')
        # print(box_title)
        # 方式2:正则
        pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
        match = pattern.search(box_title)
        # print(match)
        if match != None:
            date = match.group(1)
            real_title = match.group(2)
            # print(date,real_title)
            content = (h2_title,real_title,href,date)
            # print(content)
            rows.append(content)

headers = ['title','real_title','href','date']
# newline加上这个可以避免空行的出现
with open('gcd.csv','a',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)