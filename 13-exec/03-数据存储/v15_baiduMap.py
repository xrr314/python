'''
baidu地图api
http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi


地点详情检索服务
http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥
矩形区域检索
http://api.map.baidu.com/place/v2/search?query=银行&bounds=39.915,116.404,39.975,116.414&output=json&ak={您的密钥}

我的ak
sxEc3s8YbI9xPlmXxCn00yezH5ZmK45k


基础地址
http://api.map.baidu.com/place/v2/search?
参数:
    query:公園
    region:成都市
    scope:2
        检索结果详细程度。取值为1 或空，则返回基本信息；取值为2，返回检索POI详细信息
    page_size:20
    output:json
        输出格式为json或者xml
    ak:sxEc3s8YbI9xPlmXxCn00yezH5ZmK45k
'''

import requests


def getjson(loc,page_num=0):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    data = {
        'query':'公園',
        'region':loc,
        'scope':2,
        'page_size':20,
        'page_num':page_num,
        'output':'json',
        'ak':'sxEc3s8YbI9xPlmXxCn00yezH5ZmK45k'
    }
    base_url = 'http://api.map.baidu.com/place/v2/search?'
    res = requests.get(base_url,params=data,headers=headers)
    decodejson = res.json()
    return decodejson

a = getjson('成都市')
print(a)