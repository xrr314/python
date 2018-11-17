from  urllib import request
from  bs4 import BeautifulSoup

url= 'http://www.baidu.com'

rsp=request.urlopen(url)
content=rsp.read()

soup = BeautifulSoup(content,'lxml')

print(soup.prettify())
print('=='*20)

titles=soup.select("title")
print(titles)
meta=soup.select("meta[content='always']")
print(meta)
# soup.select("")