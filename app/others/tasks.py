#coding=utf-8
'''
Created on 2015年6月16日
all tasks
@author: hzwangzhiwei
'''
from app.wraps.async_task_wrap import async_task


@async_task
def count_to_10000():
    for i in xrange(10000):
        print i

