from  urllib import request
from  bs4 import BeautifulSoup

url= 'http://www.baidu.com'

rsp=request.urlopen(url)
content=rsp.read()

soup = BeautifulSoup(content,'lxml')

content=soup.prettify()

print(content)
print("* "*20)
print(soup.meta)
print("* "*20)
print(soup.head)
print("* "*20)
print(soup.link)
print("* "*20)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
print("* "*20)
print(soup.title.string)

print("* "*20)
print(soup.name)
print(soup.attrs)
print(soup.name)