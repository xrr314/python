from  urllib import request
from  bs4 import BeautifulSoup
import re

url= 'http://www.baidu.com'

rsp=request.urlopen(url)
content=rsp.read()

soup = BeautifulSoup(content,'lxml')

print(soup.name)
print("=="*20)
tags=soup.find_all(name='meta')
print(tags)
print("=="*20)
tags=soup.find_all(re.compile(r'^me'),content='always')
for tag in tags:
    print(tag)