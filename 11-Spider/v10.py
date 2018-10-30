'''



'''
from urllib import request,error

if __name__ == '__main__':
    url='http://www.baidu.com'

    #使用代理的步骤
    # 1. 设置代理地址
    proxy={'http':'39.137.2.234'}

    # 2. 创建proxy_handler
    proxy_handler=request.ProxyHandler(proxy)

    # 3. 创建opener
    opener=request.build_opener(proxy_handler)

    # 4. 安装opener
    request.install_opener(opener)

    #现在就正常的操作就好
    try:
        rsp=request.urlopen(url)
        html=rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
