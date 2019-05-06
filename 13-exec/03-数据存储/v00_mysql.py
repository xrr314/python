'''
mysql demo
1.获取数据库
2.获取记录
3.增加记录
4.修改记录
5.删除记录
.......
'''

import pymysql

class MysqlAPI(object):
    # 设置链接参数,设置数据库默认编码为utf8
    def __init__(self,host,username,password,dbname,port=3306):
        self.conn = pymysql.connect(host,username,password,dbname,port,charset='utf8')
        self.cursor = self.conn.cursor()

    # 获取数据
    def get_all(self,sql):
        '''
        查询所有
        :param sql:
        :return:
        '''
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            return '查询异常:{}'.format(e)

    def get_one(self,sql):
        '''
        查询一条记录
        :param sql:
        :return:
        '''
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            return '查询异常:{}'.format(e)

    def insert(self,table_name,data):
        '''
        :param table_name:
        :param data:字典的格式
        :return:
        '''
        keys = ''
        if len(data)==1:
            sql = 'insert into {}{} values'.format(table_name, tuple(data.keys())[0]).replace("'") + '{}'.format(tuple(data.values())[0])
        else:
            sql = 'insert into {}{} values'.format(table_name, tuple(data.keys())).replace("'",'') + '{}'.format(tuple(data.values()))
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return int(self.cursor.lastrowid)
        except Exception as e:
            self.conn.rollback()
            return '插入失败:{}'.format(e)


    def update(self,table_name,data,restrication):
        '''
        更新记录 tablename,data(字典),条件
        :param table_name: 表
        :param data: 更新字段(字典类型)
        :param restrication: 更新条件
        :return:
        '''
        data_str=''
        for item in data.items():
            data_str+='{}="{}",'.format(item[0],item[1])
        values = data_str[:-1]
        sql = 'update {} set {} where {}'.format(table_name,values,restrication)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            return '更新失败:{}'.format(e)

    def query(self,sql):
        '''
        执行一条sql
        :param sql:
        :return:
        '''
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return int(self.cursor.lastrowid)
        except Exception as e:
            self.conn.rollback()
            print('执行失败:{}'.format(e))

    def delete(self,table_name,restrication):
        '''
        删除表
        :param table_name: 表名
        :param restrication: 条件
        :return:
        '''
        sql = 'delete from {} where {}'.format(table_name,restrication)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            return '删除失败:{}'.format(e)

    def format_tab(self,table_name):
        '''
        格式化表格(去除所有数据,只留下表格式)
        :param table_name:
        :return:
        '''
        sql = 'trncat {}'.format(table_name)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return '{}--格式化成功'.format(table_name)
        except Exception as e:
            self.conn.rollback()
            return '{}--格式化失败'.format(table_name)

if __name__ == '__main__':
    mysql = MysqlAPI('127.0.0.1','root','123456','青马驿站')
    # print(mysql)
    for i in range(10):
        data = {
            'FIRST_NAME':'{}'.format(str(i)),
            'LAST_NAME':'AA',
            'AGE':18,
            'SEX':'N',
            'INCOME':'5555'
        }
        result = mysql.insert('tlxy',data)
        print(result)