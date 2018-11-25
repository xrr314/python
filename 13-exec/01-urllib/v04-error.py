from urllib import error,request

try:
    base_url = 'http://www.w3school.com.cn/json/index.jsp'
    response = request.urlopen(base_url)
    # 制作一个编码错误
    content = response.read().decode()
    print(content)
except error.HTTPError as e:
    print(e)
except error.URLError as e:
    print('URL异常')