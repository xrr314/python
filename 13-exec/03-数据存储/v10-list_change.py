a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

'''
要求1,4,7为一个整体
2,5,8为一个整体
3,6,9为一个整体
'''
# 方法1
for x,y,z in zip(a,b,c):
    print(type(zip(a,b,c)))
    print(x,y,z)

# 方法2
a = ['A','B','C']
b = [1,2,3]
try:
    pass
except:
    pass

x = dict(zip(a,b))
print(x)
print(type(x))