#coding=utf-8
'''
Created on 2015年6月16日

@author: hzwangzhiwei
'''
from app import app
from app.dbs import test_dbs
from app.others import tasks
from app.utils import OtherUtil

@app.route('/', methods=['GET'])
def index_page():
    #async task
    tasks.count_to_10000()
    #此处应该渲染首页模版
    try:
        rst = test_dbs.get_test_by_id('1')
    except:
        rst = {}
    return OtherUtil.object_2_dict(rst)

#定义404页面
@app.errorhandler(404)
def page_not_found(error):
    return '404'

@app.errorhandler(502)
def server_502_error(error):
    return '502'


@app.route('/not_allow', methods=['GET'])
def deny(error):
    return 'You IP address is not in white list...'