#包含一个学生类
#一个sayHello函数
#打印语句

class Student():
    def __init__(self,name='Noname',age=18):
        self.name=name
        self.age=age

    def sayHello(self):
        print('My name is {0}'.format(self.name))

def sayHello():
    print('Hi ,图灵学院')

print('我是模块p02')