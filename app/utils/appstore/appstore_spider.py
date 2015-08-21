#coding=utf-8
'''
Created on 2015年8月21日
appstore爬虫，根据appstore的id，爬取关于app的所有信息
@author: hzwangzhiwei
'''
from time import sleep
import requests
from app.lib.pyquery import PyQuery
from app.utils import Util



def _get_appstore_url(appid):
    '''
    ps：获取appstre的链接
    '''
    tpl = "https://itunes.apple.com/cn/app/biao-yan-da-ren/id%s?mt=8"
    if appid:
        return tpl % str(appid)
    return False


def _get_pyquery_doc(url):
    '''
    ps:pyquery爬虫对象
    '''
    #防止被服务器拒绝，被执行一个暂停0.1秒
    sleep(0.1)
    html = requests.get(url).text
    doc = PyQuery(html)
    return doc


def get_app_info(appid, res_dir = ""):
    '''
    ps:获得app在appstore的详细信息
    title:游戏名字
    icon:游戏图标
    author:开发商
    type:类型，例如游戏
    price:免费或者价格
    description:内容提要
    wesite:开发者网站
    pub_date:发布时间
    version:包版本号
    size:包体大小
    lang:语言，例如简体中文, 英语
    requirements:兼容性
    rate:app评级，例如：限4岁以上
    copyright:版权所属
    ratings：用户评分
    review：评分数量
    iphone_screenshot:iphone棘突
    ipad_screenshot:ipad截图
    '''
    try:
        url = _get_appstore_url(appid)
        if not url:
            return False
        
        doc = _get_pyquery_doc(url)
        
        info = {}
        
        info['title'] = doc('div#title h1').text().strip()
        info['icon'] = doc('div#left-stack div.artwork img').attr('src')
        info['author'] = doc('#left-stack > div.lockup.product.application > ul > li:nth-child(7) > span:nth-child(2) > span').text().strip()
        info['type'] = doc('#left-stack > div.lockup.product.application > ul > li.genre > a').text().strip()
        info['price'] = doc('#left-stack > div.lockup.product.application > ul > li:nth-child(1) > span > div').text().strip()
        info['description'] = doc('#content > div > div.center-stack > div.product-review p').html()
        info['wesite'] = doc('#content > div > div.center-stack > div.app-links > a').attr('href')
        info['pub_date'] = doc('#left-stack > div.lockup.product.application > ul > li.release-date > span:nth-child(2)').text().strip()
        info['version'] = doc('#left-stack > div.lockup.product.application > ul > li:nth-child(4) > span:nth-child(2)').text().strip()
        info['size'] = doc('#left-stack > div.lockup.product.application > ul > li:nth-child(5)').text().strip()
        info['lang'] = doc('#left-stack > div.lockup.product.application > ul > li.language').text().strip()
        info['requirements'] = doc('#left-stack > div.lockup.product.application > p > span:nth-child(2)').text().strip()
        info['rate'] = doc('#left-stack > div.lockup.product.application > div.app-rating > a').text().strip()
        info['copyright'] = doc('#left-stack > div.lockup.product.application > ul > li.copyright').text().strip()
        info['ratings'] = doc('#left-stack > div.extra-list.customer-ratings > div.rating > span:nth-child(1)').text().strip()
        info['review'] = doc('#left-stack > div.extra-list.customer-ratings > div.rating > span.rating-count').text().strip()
        
        info['iphone_screenshot'] = []
        iphone_screenshot = doc('div#content div.iphone-screen-shots div.lockup')
        for iphone_screen_doc in iphone_screenshot:
            info['iphone_screenshot'].append(PyQuery(iphone_screen_doc)('img').attr('src'))
        
        info['ipad_screenshot'] = []
        ipad_screenshot = doc('div#content div.ipad-screen-shots div.lockup')
        for ipad_screen_doc in ipad_screenshot:
            info['ipad_screenshot'].append(PyQuery(ipad_screen_doc)('img').attr('src'))
        
        return info
    except Exception, e:
        print e
        return False
    
if __name__ == '__main__':
    info = get_app_info(983934283)
    print Util.object_2_dict(info)
    
    info = get_app_info(1016774219)
    print Util.object_2_dict(info)
    