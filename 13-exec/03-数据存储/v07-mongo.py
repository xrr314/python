'''
mongodb:(非关系数据库)
        更加适合爬虫的数据库
        分布式数据库
        主要为web应用提供高性能的数据存储方案


SQL	        MongoDB	        解释/说明
database	database	数据库
table	    collection	表/集合
row	        document	行/文档
column	    field	    字段(列)/域
index	    index	    索引
primary     primary	    主键/MongoDB自动将_id字段设置为主键

mongodb安装(我们这里已经安装了)
    1.https://jingyan.baidu.com/article/e5c39bf5f5ddd539d76033a9.html
    2.sudo apt-get install mongodb

'''

import pymongo

# # 查询
# # 连接数据库(3种方式)
# # 默认连接本地
# # client = pymongo.MongoClient()
# client = pymongo.MongoClient('127.0.0.1',27017)
# # client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
#
# # 获取数据库
# db = client.Dengzi
# # 获取集合
# std = db.students
#
# # 获取数据
# datas = std.find()
# print(datas,type(datas))
# for data in datas:
#     print(data['name'],data['age'])

# 插入文档(行)
client = pymongo.MongoClient()

db = client.test
std = db.person
post = {
    'name':'xue',
    'age':18,
    'sex':'男',
    'class':['database','python','java','math'],
    'income':5555
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print('post_id:%s'%(post_id))

