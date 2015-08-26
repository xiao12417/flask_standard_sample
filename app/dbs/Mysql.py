#coding=utf-8
'''
Created on 2015年8月21日

@author: hzwangzhiwei
'''

import MySQLdb
from app import db_config
from functools import wraps
import time

################单例
db_instance = None
def mysql_singleton(cls):
    global db_instance
    def _singleton( *args, **kw):
        global db_instance
        if not db_instance:
            db_instance = cls(*args, **kw)
        return db_instance
    return _singleton
################单例end


#检查连接是否存在，不存在就直接返回Flase，防止多余的trace信息
def check_connect(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if args[0].conn and args[0].cursor:
            func = f(*args, **kwargs)
            return func
        return (lambda :False)()
    return decorated_function


@mysql_singleton
class Mysql():
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
    
    
    def dict_2_sql(self, table_name, dict_param):
        key = []
        val = []
        for i in range(len(dict_param)):
            key.append(dict_param.keys()[i])
            val.append("'" + str(dict_param.values()[i]) + "'")
        key = ",".join(key)
        val = ",".join(val)
        sql = "insert into " + table_name + "("+ key+") values (" + val + ");"
        return sql
    
    
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
    def exec_insert_dict(self, table_name, dict_param):
        '''
        ps:执行插入数据，数据由一个dict给定，key为column名称
        '''
        try:
            sql = self.dict_2_sql(table_name, dict_param)
            return self.exec_insert(sql, ())
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
            if row_count == False:
                row_count = True
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
        #销毁单例
        global db_instance
        db_instance = None

#test        
if __name__ == '__main__':
    start = time.time()
    
    for i in xrange(1000):
        sql = "insert into abtest_users(user_type) values(%s)"
        params = (str(i), )
        Mysql().exec_insert(sql, params)
        Mysql().close()
    
    end = time.time()
    
    print 1000 / (end - start)
#         
#     sql = "update abtest_users set user_type = 5 where user_id <= 5"
#     params = () 
#     print Mysql().exec_update(sql, params)
#     
#     sql = "select * from abtest_users where user_id <= 5"
#     params = ()
#     print Mysql().exec_select(sql, params)
#     print Mysql().exec_select_one(sql, params)