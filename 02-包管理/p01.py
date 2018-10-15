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

#如果该文件作为主进程时,执行下面的代码,如果作为import时,不执行
if __name__ == '__main__':
    print('我是模块p01')