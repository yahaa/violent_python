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

tt = 1
user_pass = pika.PlainCredentials('guest', 'guest')
conn_params = pika.ConnectionParameters('localhost', credentials=user_pass)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
channel.exchange_declare(exchange='dianping_ex', type='direct',
                         passive=False, durable=True, auto_delete=False)

channel.queue_declare(queue='dianping_qu')
channel.queue_bind(queue='dianping_qu', exchange='dianping_ex',
                   routing_key='dianping_key')

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='XS',
)
cur = conn.cursor()


def get_latest_com(url):
    print '正在爬　%s ......' % url
    res = requests.get(url)
    selector = scrapy.Selector(res)
    time = ''
    try:
        time = selector.xpath(
            '//div[@class="misc-info"]/span[@class="time"]/text()').extract()[0]
    except:
        pass
    m = re.compile(r'\d\d-\d\d')
    res = m.findall(time)
    if res:
        return res[0]
    return "no data"


def push_to_database(urls):
    try:
        for item in urls:
            try:
                url = item['url']
                time = get_latest_com(url)
                sid = item['sid']
                sql = 'update dianping set store_latest_com="' + \
                    time + '" where store_id="' + sid + '"'
                cur.execute(sql)
                print '插入数据库中　...'
            except Exception, e:
                print e
                continue
    except Exception, e:
        print e
    conn.commit()
    global tt
    print 'finish %d' % tt
    tt += 1


def get_msg(channel, method, header, body):
    urls = json.loads(body)
    push_to_database(urls)


def start_do():
    channel.basic_consume(get_msg, queue='dianping_qu', no_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    print 'start ......'
    start_do()
    # print
    # get_latest_com('http://www.dianping.com/shop/9980089/review_more_latest')
