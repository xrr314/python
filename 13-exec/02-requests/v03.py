'''
妹子图爬取
www.mzitu.com
通过换页面
https://www.mzitu.com/page/2/
https://www.mzitu.com/page/3/
可以推导出页面的方式
'''
import requests
from lxml import etree
import time,os,urllib3,random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def mz_spider(base_url,headers):
    rsp = requests.get(base_url,verify=False)
    html = etree.HTML(rsp.text)
    # print(rsp.text)
    # 获取详情页地址
    img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for img_url in img_src:
        # print(img_url)
        image_parse(img_url)


def image_parse(img_url):
    headers = {
        'User-Agent': random.choice(user_agent_list),
        'Host':'www.mzitu.com',
        'Referer':'https://www.mzitu.com/'
    }
    rsp = requests.get(img_url,headers,verify=False)
    html = etree.HTML(rsp.text)

    # 获取标题
    title = html.xpath('//h2[@class="main-title"]/text()')[0]
    # print(title)
    # 获取总页数
    pagemax = html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
    # print(pagemax)

    # 拼接图片详情页
    for num in range(1,int(pagemax)+1):
        img_src = img_url + "/" +str(num)
        # print(img_src)
        download_img(img_src,title)


# 下载图片
def download_img(img_src,title):
    rsp = requests.get(img_src,verify=False,headers=headers)
    html = etree.HTML(rsp.text)

    # 获取图片链接地址
    img_url = html.xpath('//div[@class="main-image"]/p/a/img/@src')[0]

    # 下载路径
    root_dir = 'mz_img'
    # 图片名
    img_name = img_url.split('/')[-1]
    # print(img_name)
    # 去除title中的空格
    title = title.replace(' ','')

    root_dir = root_dir+'/'+title
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)

    rsp = requests.get(img_url,headers = headers,verify=False)
    with open(root_dir+'/'+img_name,'wb') as f:
        f.write(rsp.content)
        f.close()
        print(title+"--"+img_name+"文件下载成功")


user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    ]

if __name__ == '__main__':
    headers = {
        'User-Agent': random.choice(user_agent_list),
        'Host':'www.mzitu.com',
        'Referer':'https://www.mzitu.com/'
    }
    for i in range(1,2):
        base_url = 'https://www.mzitu.com/page/{}'.format(str(i))
        time.sleep(3)
        mz_spider(base_url,headers)