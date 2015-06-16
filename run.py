#coding=utf-8
'''
Created on 2014年7月19日
一个flask 的sample
@contact: http://50vip.com
'''


from app import app
if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug = True,  threaded = True)

