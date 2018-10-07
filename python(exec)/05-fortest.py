import math
import random

#输入函数
num=input('请输入一个数字')
#输入内容为str类型,需要进行类型转换
num=int(num)
if num>=100 and num<1000:
    print('输入正确')
else:
    print('输入错误')