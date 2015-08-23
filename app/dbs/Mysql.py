#coding=utf-8
'''
Created on 2015年8月21日

@author: hzwangzhiwei
'''

import MySQLdb
from app.wraps.singleton_wrap import singleton
from app import db_config
from functools import wraps

#数据库配置，配置统一放到app/__init__中
# db_config = {
#     'DB_USER': 'dev',
#     'DB_PSW': 'dev',
#     'DB_NAME': 'ab_test',
#     'DB_HOST': '10.246.14.121',
#     'DB_PORT': 3306,
#     'DB_CHARSET': 'utf8'
# }

#检查连接是否存在，不存在就直接返回Flase，防止多余的trace信息
def check_connect(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if args[0].conn and args[0].cursor:
            func = f(*args, **kwargs)
            return func
        return (lambda :False)()
    return decorated_function
        
@singleton
class Mqsql:
    #对象属性
    #连接
    conn = None
    #数据游标
    cursor = None
    
    #构造函数
    def __init__(self, host = db_config['DB_HOST'], 
                        port = db_config['DB_PORT'],
                        user = db_config['DB_USER'], 
                        passwd = db_config['DB_PSW'], 
                        db = db_config['DB_NAME'], 
                        charset = db_config['DB_CHARSET']):
        
        try:
            self.conn = MySQLdb.connect(host = host, port = port, user = user, passwd = passwd, db = db, charset = charset)
            #字典形式
            self.cursor = self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
            print("Mysql Connect to %s: %s" % (host, str(port)))
        except MySQLdb.Error as e:
            print("Mysql Error %s: %s" % (host, e.args[1]))

    @check_connect
    def exec_select(self, sql, params):
        '''
        ps：执行查询类型的sql语句
        '''
        try:
            self.cursor.execute(sql, params)
            result_set = self.cursor.fetchall()
            return result_set
        except MySQLdb.Error as e:
            print("Mysql Error:%s\nSQL:%s" %(e, sql))
            return False
        
    @check_connect
    def exec_select_one(self, sql, params):
        '''
        ps：执行查询类型的sql语句
        '''
        try:
            self.cursor.execute(sql, params)
            result_set = self.cursor.fetchone()
            return result_set
        except MySQLdb.Error as e:
            print("Mysql Error:%s\nSQL:%s" %(e, sql))
            return False
    @check_connect
    def exec_insert(self, sql, params):
        '''
        ps:执行插入类sql语句
        '''
        try:
            # 执行sql语句
            self.cursor.execute(sql, params)
            # 提交到数据库执行
            insert_id = self.conn.insert_id()
            self.conn.commit()
            return insert_id
        except MySQLdb.Error as e:
            print("Mysql Error:%s\nSQL:%s" %(e, sql))
            self.conn.rollback()
            return False
    @check_connect
    def exec_update(self, sql, params):
        '''
        ps:执行更新类sql语句
        '''
        try:
            # 执行sql语句
            self.cursor.execute(sql, params)
            row_count = self.cursor.rowcount
            # 提交到数据库执行
            self.conn.commit()
            return row_count
        except MySQLdb.Error as e:
            print("Mysql Error:%s\nSQL:%s" %(e, sql))
            self.conn.rollback()
            return False
    ###################
    ###################
    @check_connect
    def exec_sql(self, sql, params):
        try:  
            n = self.cursor.execute(sql, params)  
            return n  
        except MySQLdb.Error as e:  
            print("Mysql Error:%s\nSQL:%s" %(e, sql))
    
    @check_connect
    def get_last_insert_id(self):
        '''
        ps:最后插入行id
        '''
        return self.conn.insert_id()
    
    @check_connect
    def get_influence_row_count(self):
        '''
        ps:影响函数
        '''
        return self.cursor.rowcount  
    #for transation
    @check_connect
    def commit(self):
        '''
        PS:事物完成之后，commit
        '''
        self.conn.commit()
    
    @check_connect    
    def rollback(self):
        '''
        PS:事物失败之后，回退
        '''
        self.conn.rollback()
    #end for transation
    ###################
    ###################
    
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


#test        
if __name__ == '__main__':
    for i in xrange(10):
        sql = "insert into abtest_users(user_type) values(%s)"
        params = (str(i), )
        print Mqsql().exec_insert(sql, params)
    sql = "update abtest_users set user_type = 5 where user_id <= 5"
    params = () 
    print Mqsql().exec_update(sql, params)
    
    sql = "select * from abtest_users where user_id <= 5"
    params = ()
    print Mqsql().exec_select(sql, params)
    print Mqsql().exec_select_one(sql, params)