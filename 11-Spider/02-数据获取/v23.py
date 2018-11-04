'''
python中的正则模块re
使用步骤:
1.compile函数正则表达式的字符串便以为一个pattern对象
2.通过pattern对象的一些方法对文本进行匹配,匹配结果是match对象
3.用match对象的方法,对结果进行操作
'''
import  re
#\d表示
s = r"\d+" #r表示后面内容不需要转义,在每一次写re表达式的时候都要加上

#返回一个pattern对象
pattern = re.compile(s)

#返回一个match对象
m= pattern.match("one12two2three3")

print(type(m))
print(m)


#返回一个match对象
#后面为位置参数表示开始和结束的位置
m= pattern.match("one12two2three3",3,10)

print(type(m))
print(m)

print(m.group())
print(m.start(0))
print(m.end(0))
print(m.span(0))