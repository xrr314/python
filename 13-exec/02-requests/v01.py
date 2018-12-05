'''
京东商品
https://item.jd.com/1250438.html
请求方式requests.get()/requests.post()
请求参数:
    url
    数据携带
        post:data    传递参数(不需要编码)
        get:params=字典类型
    proxies 设置代理
    auth=('usr','pass') 客户端认证(使用很少)
    verify=True 免除ssl认证

返回值属性:
    rsp.status_code 查看响应编码
    rsp.text    响应内容(字符串)
    rsp.content 得到相应内容(字节流)
    rsp.url 获取完整url地址
    rsp.apparent_encoding   获取编码格式
        解决页面乱码
    rsp.cookie  获得cookieJar对象
        使用requests.utils.dict_from_cookieJar(cookieJar对象)获得一个字典类型
'''

import requests

url = 'https://item.jd.com/1250438.html'

try:
    # 发起get请求
    rsp = requests.get(url)

    print(rsp.content)

except:
    pass