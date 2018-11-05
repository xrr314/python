'''
search
'''

import re

s = r'\d+'

pattern = re.compile(s)

#参数表明起止位置
m = pattern.search("one12two23three 45")

print(m.group())

#参数表明起止位置
m = pattern.search("one12two23three56",10,40)

print(m.group())