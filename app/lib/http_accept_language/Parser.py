#coding=utf-8
'''
Created on 2015年8月25日

@author: hzwangzhiwei
'''
import re

class AcceptLangParser(object):
    '''
    classdocs
    '''
    regex = r'([a-zA-Z|-]{1,8})(;s*qs*=s*(1|0.[0-9]+)){0,1}'
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def get_langs(self, http_accept_lang):
        langs = []
        if not http_accept_lang:
            return langs
        match = re.findall(self.regex, http_accept_lang)
        for m in match:
            langs.append({'lang': m[0], 'q': m[2] or '1.0'})
            
        return langs
    
    def get_lang(self, http_accept_lang):
        langs = self.get_langs(http_accept_lang)
        if len(langs) == 0:
            return ""
        else:
            if 'lang' in langs[0].keys():
                return langs[0]['lang']
            return ""
        
if __name__ == '__main__':
    print AcceptLangParser().get_langs('zh-CN,zh;q=0.8,en;q=0.6')
    print AcceptLangParser().get_lang('zh-CN,zh;q=0.8,en;q=0.6')
    