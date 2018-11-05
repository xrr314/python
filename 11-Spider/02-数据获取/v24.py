
import re
s = r'([a-z]+)([a-z]+)'
pattern = re.compile(s,re.I)#s.I忽略大小写
m=pattern.match("hello world wide web")


#表示返回匹配成功的子串
s=m.group(0)
print(s)

#返回匹配成功的子串的跨度
a=m.span(0)
print(a)

#表示返回匹配成功的子串
s=m.group(1)
print(s)

#返回匹配成功的子串的跨度
a=m.span(1)
print(a)

s=m.groups()
print(s)