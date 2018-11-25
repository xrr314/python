import math
#ceil向上取整
print(math.ceil(5.1))
#floor向下取整
print(math.floor(5.1))

#查看系统保留关键字)
import keyword
print(keyword.kwlist)

#round四舍五入
print(round(5.4))

#sqrt开方
print(math.sqrt(9))

#pow幂运算
print(math.pow(4,0.5))
print(4**0.5)

#fabs绝对值,返回浮点数
print(math.fabs(-3))

#abs获取绝对值,类型不改变,内置函数
print(abs(-3))

# fsum()对整个序列去和
print(math.fsum([1,2,3,4]))
#sum内置函数
print(sum([1,2,3]))

#modf将一个浮点数拆分为整数和小数
print(math.modf(5.4))
help(math.modf)

#copysign将第二个数的符号(正负号)传给第一个数
print(math.copysign(2,-3))




import random

#random获取0-1之间的随机小数
for i  in range(10):
    print(random.random())
    print(random.randint(1,9))
    print(random.randrange(1,9,2))
print('*'*20)

#choice()随机获取列表中的值
l=[1,2,3,4,5,6,7,8,9,0]
print(random.choice(l))
print('*'*20)

#shuffle()随机打乱序列
random.shuffle(l)
l1=l.copy()
print(l1)
print('*'*20)

#uniform()随机获取指定范围内的值
print(random.uniform(1,9))

