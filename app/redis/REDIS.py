#coding=utf-8
'''
Created on 2015年8月21日
Redis操作的库
@author: hzwangzhiwei
'''
#数据库配置
from app.wraps.singleton_wrap import singleton


@singleton
class REDIS:
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

    
