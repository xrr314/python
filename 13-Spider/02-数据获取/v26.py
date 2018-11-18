'''
findall
'''

import re

pattern = re.compile(r'\d+')

m = pattern.findall('i am 18 years old and 185 high')

print(m)

m = pattern.finditer('i am 18 years old and 185 high')

print(type(m))
for i in m:
    print(i.group())