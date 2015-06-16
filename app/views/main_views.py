#coding=utf-8
'''
Created on 2015年6月16日

@author: hzwangzhiwei
'''
import flask

from app import app
from app.dbs import main_dbs
from app.others.tasks import count_to_10000


@app.route('/', methods=['GET'])
def index_page():
    #async task
    count_to_10000()
    #此处应该渲染首页模版
    return flask.jsonify(main_dbs.get_user_by_id('hzwangzhiwei'))

#定义404页面
@app.errorhandler(404)
def page_not_found(error):
    return '404'

@app.errorhandler(502)
def server_502_error(error):
    return '502'
