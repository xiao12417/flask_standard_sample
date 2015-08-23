#coding=utf-8
'''
Created on 2015年8月21日

@author: hzwangzhiwei
'''

from pymongo import Connection
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
        if args[0].conn and args[0].db:
            func = f(*args, **kwargs)
            return func
        return (lambda :False)()
    return decorated_function
        
@singleton
class Mongo:
    #对象属性
    #连接
    conn = None
    #数据游标
    db = None
    
    #构造函数
    def __init__(self, host = db_config['DB_HOST'], 
                        port = db_config['DB_PORT'],
                        user = db_config['DB_USER'], 
                        passwd = db_config['DB_PSW'], 
                        db = db_config['DB_NAME'], 
                        charset = db_config['DB_CHARSET']):
        
        try:
            self.conn = Connection(host = host, port = port, user = user, passwd = passwd, db = db, charset = charset)
            #字典形式
            self.db = self.conn[db]
            print("MongoDB Connect to %s: %s" % (host, str(port)))
        except Exception, e:
            print("MongoDB Error %s: %s" % (host, e.args[1]))

    @check_connect
    def exec_select(self, table, params, sort):
        '''
        ps：执行查询类型
        '''
        try:
            result_set = self.db[table].find(params).sort(sort)
            return result_set
        except Exception, e:
            print("MongoDB Error %s: %s" % (host, e.args[1]))
            return False
        
    @check_connect
    def exec_select_one(self, table, params):
        '''
        ps：执行查询类型的sql语句
        '''
        try:
            result_set = self.db[table].find(params)
            return result_set
        except Exception, e:
            print("MongoDB Error %s: %s" % (host, e.args[1]))
            return False

    @check_connect
    def exec_insert(self, table, params):
        '''
        ps:执行插入类sql语句
        '''
        try:
            r = self.db[table].insert(params)  
            return r
        except Exception, e:
            print("MongoDB Error %s: %s" % (host, e.args[1]))
            return False

    @check_connect
    def exec_update(self, table, params):
        '''
        ps:执行更新类sql语句
        '''
        try:
             r = self.db[table].update(params)
             return r
        except Exception, e:
            print("MongoDB Error %s: %s" % (host, e.args[1]))
            return False
    
     @check_connect
    def exec_count(self, table, params):
        '''
        ps:执行更新类sql语句
        '''
        try:
             r = self.db[table].count(params)
             return r
        except Exception, e:
            print("MongoDB Error %s: %s" % (host, e.args[1]))
            return False

    
    def close(self):
        pass


#test        
if __name__ == '__main__':
    #TODO
    pass