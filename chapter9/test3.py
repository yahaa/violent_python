# -*- coding: utf-8 -*-
# def log(func):
#     def wra(*args, **kw):
#         print "call %s()" % func.__name__
#         return func(*args, **kw)
#     return wra
#
#
# def now():
#     print "2017-6-4"
#
#
# now = log(now)


import json
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'YgPGvHf33XbLnbAVZMzyXMaC5xXEHdwU'
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    print uri
    req = requests.post(uri)
    print req.text
    jso = json.loads(req.text)
    print tuple(jso['result']['location'])


getlnglat('上海')
