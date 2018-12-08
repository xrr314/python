'''
之前我们常用的是
open(filename,'wb) as f:
    f.write(xxx)
这边我们使用urllib模块的方法进行音频文件下载
request.urlretrieve()
也可以讲远程数据下载到本地
方法参数:url, filename=None, reporthook=None, data=None
    url:下载的url地址
    filebname:存储路径+文件名
    reporthook:设置回调函数
        链接上服务器或者响应下载完毕时触发回调函数
        用得最多的是显示下载进度
    data:(filename,headers)
        返回元组
'''
'''
爬取天堂网图片-自然风光
http://www.ivsky.com/tupian/ziranfengguang/
可以根据翻页查看url的变化
http://www.ivsky.com/tupian/ziranfengguang/index_2.html
http://www.ivsky.com/tupian/ziranfengguang/index_3.html
'''

from urllib import request
from lxml import etree
import os,requests


def Schedule(blocknum, blocksizem, totalsize):
    '''
    显示下载进度
    :param blocknum: 已经下载的数据块
    :param blocksizem: 数据块大小
    :param totalsize: 远程文件大小
    :return:
    '''
    per = 100.0 * blocknum * blocksizem / totalsize
    if per>100:
        per = 100
    print("当前下载进度:{0}".format(per))

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
url = 'http://www.ivsky.com/tupian/ziranfengguang/'

rsp = requests.get(url,headers=headers)

html = etree.HTML(rsp.text)
img_urls = html.xpath('//ul[@class="ali"]/li/div/a/img/@src')
# print(img_src)
for img_url in img_urls:
    root_dir = 'v05-img'
    # 创建保存根路径目录
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    filename = img_url.split('/')[-1]
    request.urlretrieve(img_url,root_dir+'/'+filename,Schedule)




