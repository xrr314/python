from urllib import request
from lxml import etree

base_url = 'http://zuihaodaxue.com/zuihaodaxuepaiming2018.html'

rsp = request.urlopen(base_url)
html = rsp.read().decode()

html = etree.HTML(html)
items = html.xpath('//tr[@class="alt"]')
for item in items:
    # 排名
    number = item.xpath('./td')[0].text
    # 学校
    school = item.xpath('./td')[1].text
    # 省份
    province = item.xpath('./td')[2].text
    # 总分
    score = item.xpath('./td')[3].text
    print(str(number)+'--'+str(school)+'--'+str(province)+'--'+str(score))