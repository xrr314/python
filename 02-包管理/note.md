# 1 模块
- 一个模块就是包含python代码的文件,后缀名为.py就可以,就是个python文件
- 为什么用模块?
    - 程序太大,编程不方便,需要拆分
    - 模块增加代码的重复利用的方式
    - 当做命名空间用,避免命名冲突
- 如何定义模块
    - 模块就是有个普通文件,所以任何代码可以直接书写
    - 不过根据模块的规范,最好在模块中写一下内容
        - 函数(单一功能)
        - 类(相似功能的组合,或者相似业务模块)
        - 测试代码
- 如何使用模块
    - 模块直接导入
        - 加入模块名称不能直接以数字开头
            - 解决方案:使用importlib.import_module('模块名')
            - 案例01,02
    - 语法
    
            import module_name
            module_name.func_name
            module_name.class_name
            案例p01,p02
            
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余同第一种方式
        - 案例p03
        
    - from module_name import func_name,class_name
        - 导入指定内容
        - 案例p04
        
    - from module_name import *
        - 导入模块类所有内容
        - 案例p05
        
- if __name__ == '__main__:的使用
    - 可以有效避免模块代码被导入时,被执行的问题
    - 建议所有程序的入口都以此代码问入口
    
# 2 模块的搜索路径和存储
- 什么是模块的搜索路径
    - 加载模块的额时候,系统会在哪些地方寻找次模块
- 系统默认的模块搜索路径

        import sys
        sys.path属性可以获取路径列表
        案例p06
        
- 添加搜索路径
    
        sys.path.append(dir)
        
- 模块加载顺序
    1.内存中加载好的模块
    2.python内置模块
    3.搜索sys.path路径
    
    
# 包
- 包是一种组织管理代码的方式,包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

        |---包
        |---|---__init__.py     包的标志文件
        |---|---模块1
        |---|---模块2
        |---|---子包(子文件夹)
        |---|---|---__init__.py
        |---|---|---子包模块1
        |---|---|---子包模块2
        
- 包的导入操作
    - import package_name
        - 直接导入一个包,可以使用__init__.py中的内容
            - 一般内容为空
        - 使用方式:
        
                package_name.func_bname
                package_name.class_name.func_name
                
        - 此种方式的访问内容是
        - 案例pkg01,p07
    - import package_name as p
        - 别名用法
        - 注意此种方法默认对__init__.py内容的导入
        
    - import package.module
        - 导入包中某个具体的模块
        - 使用方法
        
                package.module.func_name
                package.module.class.func_name
                package.module.class.var
        - 案例p08
    - import package.module as pm
- from ... import 导入
    - from package import module1,module2,...
    - 此种导入方法不执行__init__.py的内容
    
            from pkg01 import p01
            
- from pkg01 import *
    - 导入当前包'__init__.py'文件中所有函数和类
    - 使用方法
                
                func_name()
                class_name.func_name
                class_name.var
                
    - 案例p09,注意此种导入的具体内容
    
- from package.module import *
    - 导入包中指定模块的所有内容
    - 使用方式
    
            func_name
            class_name.func_name
            
- 在开发环境中经常会使用其他模块的内容,可以在当前包直接导入其他模块的内容
    - import 完整包或者模块的路径
    
- '__all__'的用法
    - 在使用from package import *的时候,*可以导入的内容
    - '__init__.py'中如果文件为空,或者没有'__all__',那么只可以吧'__init__'中的内容导入
    - '__init__'如何设置了'__all__'的值,那么按照'__all__'指定的子包或者模块进行导入,
    如此则不会载入'__init__'中的内容
    - '__all__=['module1','module2',...]'
    - 案例pkg02,p10
    
# 命名空间
- 用于区分不同位置不同功能当相同名称的函数/变量的一个特定前缀
- 作用是防止命名冲突

        setName()
        Student.setName()
        Dog.setName() 