'''
python对json文件做操分为编码和解码
编码:
dumps   字符串
dump    json对象,可以通过fp文件流写入文件
解码:
    load
    loads
'''
import json

str = "[{'usrname':'xrr','age':18}]"
print(type(str))
json_str = json.dumps(str,ensure_ascii=False)
print(json_str)
print(type(json_str))

new_str = json.loads(json_str)
print(new_str,type(new_str))