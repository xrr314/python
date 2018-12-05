'''
图片下载
'''

import requests,os
url = 'http://tc.sinaimg.cn/maxwidth.800/tc.service.weibo.com/p3_pstatp_com/6da229b421faf86ca9ba406190b6f06e.jpg'

# 保存文件夹
root = 'pics'
# 图片位置和保存文件
path = root+'/'+url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r =requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            print('图片保存完成')
    else:
        print('文件已经存在')
except :
    print('爬取失败')