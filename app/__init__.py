#coding=utf-8
'''
Created on 2015年6月16日

@author: hzwangzhiwei
'''
from flask import Flask

app = Flask(__name__)
app.secret_key = 'your_session_key_ab_test'

from app.views import main_views

db_config = {
    'DB_USER': 'dev',
    'DB_PSW': 'dev1',
    'DB_NAME': 'ab_test',
    'DB_HOST': '10.246.14.121',
    'DB_PORT': 3306,
    'DB_CHARSET': 'utf8'
}

redis_config = {
    'RD_PSW': '',
    'RD_HOST': '10.246.14.121',
    'RD_PORT': 6379,
    'TEMP_DB': 1, #缓存db
    'VISIT_DB': 2 #用户访问db
}