#coding=utf-8
'''
Created on 2015年8月21日

@author: hzwangzhiwei
'''
from app.utils.appstore import appstore_spider

from app.utils import Request
from flask.globals import request
import flask
from app import app


@app.route('/app_info.html', methods=['GET'])
def app_info_page():
    return flask.render_template('test_page/apple_spider.html')


@app.route('/app_info', methods=['GET', 'POST'])
def app_info():
    #此处应该渲染首页模版
    appid = Request.get_parameter(request, 'appid', '983934283')
    app_info = appstore_spider.get_app_info(appid)
    return flask.jsonify({'success': 1, 'data': app_info})