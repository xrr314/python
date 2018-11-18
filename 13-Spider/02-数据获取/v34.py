from  urllib import request
from  bs4 import BeautifulSoup

url= 'http://www.baidu.com'

rsp=request.urlopen(url)
content=rsp.read()

soup = BeautifulSoup(content,'lxml')

print(soup.name)
print("=="*20)

for node in soup.head.contents:
    if node.name== 'title':
        print(node.string)
        # print("==" * 20)
    if node.name=='meta':
        print(node)