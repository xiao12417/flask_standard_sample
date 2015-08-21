#coding=utf-8
'''
Created on 2015年8月21日

@author: hzwangzhiwei
'''

#获得参数，post或者get
def get_parameter(request, key, default = None):
    '''
    info:获得请求参数，包括get和post，其他类型的访问不管
    '''
    #post参数
    if request.method == 'POST':
        param = request.form.get(key, default)
    #get
    elif request.method == 'GET':
        param = request.args.get(key, default)
    else:
        return default
    
    return param