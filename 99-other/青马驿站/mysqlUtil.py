'''
mysql安装:
    sudo apt-get update
    sudo apt-get install mysql-server
    sudo apt-get install mysql-client
    sudo apt-get install libmysqlclient-dev

登录
    # 其中-u表示用户,root为使用的用户名,-p表示密码
    sudo mysql -uroot -p

mysql远程设置
    1.修改/etc/mysql/my.conf
        找到bind-address:127.0.0.1这一行注释掉
        或者设置为0.0.0.0
    2.让root用户支持远程
        登录到mysql数据库
            sudo mysql -uroot -p
        赋予权限
            1.赋予任何主机访问数据的权限
            GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'WITH GRANT OPTION
            2.想myuser使用mypassword从任何主机连接到mysql服务器的话。
            GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'IDENTIFIED BY 'mypassword' WITH GRANT OPTION;
            3.你想允许用户myuser从ip为192.168.1.6的主机连接到mysql服务器，并使用mypassword作为密码
            GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'192.168.1.3'IDENTIFIED BY'mypassword' WITH GRANT OPTION;
    3.修改生效
        FLUSH PRIVILEGES
    4.rhe17系统中需要让防火墙允许通过
        控制台下
        firewall-cmd --permanent --add-service=mysql
        firewall-cmd --reload

python操作mysql
    安装pymysql
        pip install pymysql
'''


import pymysql


# # 创建数据库
# try:
#     # 获取数据库链接,如果是utf8类型,需要定制数据库
#     # 打开链接
#     '''
#     host='127.0.0.1',   主机地址
#     user='root',        用户名
#     password='123456',  密码
#     db='青马驿站',          数据库
#     port='3306'         端口
#     '''
#     db = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='青马驿站',port=3306)
#     # 创建游标,对数据进行操作,使用cursor()方法
#     cursor = db.cursor()
#     # 使用excecute()来执行sql语句
#     cursor.execute('drop tables if exists tlxy')
#     sql = '''create table tlxy(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT
#     )'''
#     cursor.execute(sql)
#     db.close()
#
# except:
#     print('创建失败')

# # 数据插入
# db = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',port=3306,db='青马驿站')
#
# cursor = db.cursor()
# sql = 'insert into tlxy(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ("xue","rongrong",18,"M","5555"),' \
#       '("huang","laoban",19,"1",66666)'
# # 为了防止sql注入
# sql = "INSERT INTO tlxy(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) \
#       VALUES('%s','%s','%d','%c','%s')"%('xue','rongrong',18,'M','5555')
# try:
#     cursor.execute(sql)
#     # 提交执行
#     db.commit()
# except:
#     # 发生意外,事件回滚
#     db.rollback()
#     print('出错了')
# db.close()

def queryById(id):
    db = pymysql.connect('127.0.0.1', 'root', '123456', '青马驿站')
    cursor = db.cursor()
    try:
        sql = 'select * from exam where uuid = "%s"'%(id)
        cursor.execute(sql)
        # 取得查询结果,为元组类型
        data = cursor.fetchall()
        # print(data)
        return data
    except:
        return '查询失败'
    finally:
        db.close()

def insert(data):
    db = pymysql.connect('127.0.0.1', 'root', '123456', '青马驿站')
    cursor = db.cursor()
    try:
        sql = "insert into exam(uuid,optionCount,subDescript,option0,option1,option2,option3,option4,option5,score,type) VALUES('%s','%d','%s','%s','%s','%s','%s','%s','%s','%d','%s')" % (data['uuid'], int(data['optionCount']),data['subDescript'],data['option0'],data['option1'],data['option2'],data['option3'],data['option4'],data['option5'],int(data['score']),data['type'],)
        cursor.execute(sql)
        db.commit()
        return '添加成功'
    except:
        db.rollback()
        print("添加失败")
        return  '添加失败'
    finally:
        db.close()

def updatecur(id,cur):
    db = pymysql.connect('127.0.0.1', 'root', '123456', '青马驿站')
    cursor = db.cursor()
    try:
        sql = 'update exam set cur = "%s" where uuid = "%s"'%(cur,id)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("更新失败")
    finally:
        db.close()
