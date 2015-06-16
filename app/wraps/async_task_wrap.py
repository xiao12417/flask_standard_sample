#coding=utf-8
'''
Created on 2015年6月16日

@author: hzwangzhiwei
'''
from threading import Thread


def async_task(f):
    '''
    wrap with this, the function will be async
    use at task which need long time to finish
    '''
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper