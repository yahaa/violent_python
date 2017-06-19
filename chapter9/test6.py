# coding=utf-8
import re
import requests
import scrapy
import MySQLdb
import threading
import pika
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

ti = 1

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='XS',
    charset='utf8',
)
cur = conn.cursor()


def get_store_id():
    n = cur.execute(
        'select store_id,store_address from dianping where store_latest_com=""')
    ids = cur.fetchmany(n)
    return n, ids


def get_res():
    global ti
    n, sid = get_store_id()
    for item in sid:
        try:
            sid = item[0]
            url = 'http://www.dianping.com/shop/' + sid + '/review_more_latest'
            time = get_latest_com(url)
            print time
            lng, lat = get_lng_lat(item[1])
            upate_store(time, lng, lat, sid)
            print '已完成　[%d/%d]' % (ti, n)
            ti += 1
        except Exception, e:
            print e


def upate_store(time, lng, lat, sid):
    try:
        sql = 'update dianping set store_latest_com="%s",store_lng="%s",store_lat="%s" where store_id=%s' % (
            time, lng, lat, sid)
        cur.execute(sql)
    except Exception, e:
        print e
    finally:
        conn.commit()


def get_latest_com(url):
    print '获取　%s 的最新评论' % url
    res = requests.get(url)
    selector = scrapy.Selector(res)
    time = ''
    try:
        time = selector.xpath(
            '//div[@class="misc-info"]/span[@class="time"]/text()').extract()[0]
    except Exception, e:
        print e
    m = re.compile(r'\d\d-\d\d')
    res = m.findall(time)
    if res:
        return res[0]
    return "no data"


def get_lng_lat(address):
    print '获取　%s 的经纬度' % address
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'YgPGvHf33XbLnbAVZMzyXMaC5xXEHdwU'
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    req = requests.post(uri)
    jso = json.loads(req.text)
    lng = 0
    lat = 0
    try:
        lng, lat = jso['result']['location']['lng'], jso['result']['location']['lat']
    except Exception, e:
        print e
    return lng, lat


if __name__ == '__main__':
    print 'start ...'
    get_res()
