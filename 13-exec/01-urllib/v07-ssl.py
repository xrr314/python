'''
关于网站证书
部分网站需要提供ssl证书否则
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)>
'''

from urllib import request
import ssl

#ssl免认证
ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://inv-veri.chinatax.gov.cn/'
req = request.Request(url=base_url ,headers='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')
rsp = request.urlopen(req)
html = rsp.read().decode()
print(html)