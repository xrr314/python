'''
ajax异步加载
https://www.pexels.com/
通过浏览器截取每次加载的url
https://www.pexels.com/?dark=false&format=js&page=4&seed=2018-12-11+11%3A02%3A14++0000&format=js&seed=2018-12-11%2011:02:14%20+0000
https://www.pexels.com/?dark=false&format=js&page=5&seed=2018-12-11+11%3A02%3A14++0000&format=js&seed=2018-12-11%2011:02:14%20+0000
https://www.pexels.com/?dark=false&format=js&page=6&seed=2018-12-11+11%3A02%3A14++0000&format=js&seed=2018-12-11%2011:02:14%20+0000
https://www.pexels.com/?dark=false&format=js&page=7&seed=2018-12-11+11%3A02%3A14++0000&format=js&seed=2018-12-11%2011:02:14%20+0000
通过观察,我们可以尝试
https://www.pexels.com/?page=7是否能够正常访问
尝试得到https://www.pexels.com/?page=7可以作为访问的路径,我们只需要拼接后面的page=xxx就能够爬取所有的信息
通过html分析得到//div[@class="photos__column"]/article/a/img/@src
'''

import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

base_url = 'https://www.pexels.com/?page='

urls = [base_url+str(i) for i in range(1,10)]

# print(urls)
img_urls = []
for url in urls:
    rsp = requests.get(url,headers=headers)
    # print(rsp.text)
    soup = BeautifulSoup(rsp.text,'lxml')
    imgs = soup.select('div.photos__column article a img')
    for img in imgs:
        photo = img['src']
        if photo.endswith('500'):
            img_urls.append(photo)
            # print(photo)
path = 'v08_img'

for img_url in img_urls:
    img_name = img_url.split('/')[5].split('?')[0]
    print(img_name)
    rsp = requests.get(img_url,headers=headers)
    if img_name:
        fp = open(path+'/'+img_name,'wb')
        fp.write(rsp.content)
        fp.close()
        time.sleep(2)
