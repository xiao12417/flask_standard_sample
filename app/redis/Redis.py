#coding=utf-8
'''
Created on 2015年8月21日
Redis操作的库
@author: hzwangzhiwei
'''
#数据库配置
import redis
from app import redis_config
import time

class Redis:
    connect = None
    def __init__(self, host = redis_config['RD_HOST'], 
                        port = redis_config['RD_PORT'],
                        password = redis_config['RD_PSW'], 
                        db = redis_config['TEST_DB'], 
                        charset = redis_config['RD_CHARSET']):
        
        self.connect = redis.StrictRedis(host = host, port = port, password = password, db = db, charset = charset)
        print 'new redis connect to %s:%s %d' % (host, port, db)
        
    def set(self, key, value):
        return self.connect.set(key, value)
        
    def delete(self, key):
        return self.connect.delete(key)
        
    def get(self, key):
        return self.connect.get(key)
        
    def keys(self):
        return self.connect.keys()
    
    def dbsize(self):
        return self.connect.dbsize()
        
    def flushdb(self):
        return self.connect.flushdb()
    
    def exists(self, key):
        return self.connect.exists(key)
    
    #关闭，TODO
    def close(self):
        return True

#############################

class RedisQueue(object):  
    """Simple Queue with Redis Backend"""  
    def __init__(self, name, 
                        namespace = 'queue', 
                        host = redis_config['RD_HOST'], 
                        port = redis_config['RD_PORT'],
                        password = redis_config['RD_PSW'], 
                        db = redis_config['TEST_DB'], 
                        charset = redis_config['RD_CHARSET']):
        
        """The default connection parameters are: host='localhost', port=6379, db=0"""  
        self.__db= redis.Redis(host = host, port = port, password = password, db = db, charset = charset)  
        self.key = '%s:%s' %(namespace, name)  
  
    def qsize(self):  
        """Return the approximate size of the queue."""  
        return self.__db.llen(self.key)  
  
    def empty(self):  
        """Return True if the queue is empty, False otherwise."""  
        return self.qsize() == 0  
  
    def put(self, item):  
        """Put item into the queue."""  
        return self.__db.rpush(self.key, item)  
  
    def get(self, block = True, timeout = None):  
        """Remove and return an item from the queue.  
 
        If optional args block is true and timeout is None (the default), block 
        if necessary until an item is available."""  
        if block:  
            item = self.__db.blpop(self.key, timeout = timeout)  
        else:  
            item = self.__db.lpop(self.key)  
  
        if item:  
            item = item[1]  
        return item
    
    #TODO has bug
    def get_nowait(self):  
        """Equivalent to get(False)."""  
        return self.get(False)  
    
    def flush(self):
        self.__db.delete(self.key)
      
if __name__ == '__main__':
    q = RedisQueue('test')
#     q.flush()
    start = time.time()
    key = ''
    #仅仅set，22972.6616659 条每秒
    #set、get、del，大概为8000条每秒
    #几乎不随数据量大小而变慢
    for i in xrange(100):
        key = 'key' + str(i)
        q.put({'key': key})  
        print q.get(block = False, timeout = 1)
    end = time.time()
    t = end - start
    print t
    print 100000 / t
    print q.qsize()
#     q.flush()
#     print q.keys()
#     r.flushdb()
#     print r.keys()