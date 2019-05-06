'''
图形界面
navicat
    我们通常使用图形界面进行数据库/表创建
'''
import pymysql

db = pymysql.connect('127.0.0.1','root','123456','青马驿站')
cursor = db.cursor()

# 更新
# sql = 'update tlxy set AGE=AGE-1 where FIRST_NAME = "%s"'%('xue')
# 删除
sql = 'delete from tlxy WHERE FIRST_NAME = "%s"'%('xue')

try:
    cursor.execute(sql)
    db.commit()
except :
    print("更新/删除失败")
    db.rollback()
db.close()

