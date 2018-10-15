'''
定义一个学生类,用来形容学生
'''

# 定义一个空的类
class Student():
    pass

# 定义一个对象
mingyue=Student()

# 定义一个类,用来描述python学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'python'
    def doHomework(self):
        print('在做作业')
        # 推荐在函数末尾使用return语句
        return None

yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
print(yueyue.course)
yueyue.doHomework()