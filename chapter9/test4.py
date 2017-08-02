# coding=utf-8
import re
import requests
import scrapy
import MySQLdb
import threading
import pika
import sys
import json
user_pass = pika.PlainCredentials('guest', 'guest')
conn_params = pika.ConnectionParameters('localhost', credentials=user_pass)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
channel.exchange_declare(exchange='dianping_ex', type='direct',
                         passive=False, durable=True, auto_delete=False)
channel.queue_declare(queue='dianping_qu')
channel.queue_bind(queue='dianping_qu',
                   exchange='dianping_ex', routing_key='dianping_key')


def sendMsg(urls):
    urls = json.dumps(urls)
    msg_props = pika.BasicProperties()
    msg_props.content_type = "text/plain"
    channel.basic_publish(body=urls, exchange='dianping_ex',
                          properties=msg_props, routing_key='dianping_key')


conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='XS',
)
cur = conn.cursor()


def get_store_id():
    n = cur.execute(
        'select store_id from dianping where store_latest_com=""')
    ids = cur.fetchmany(n)
    return n, ids


def get_url():
    n, sid = get_store_id()
    res = []
    for i in sid:
        i = i[0]
        url = {'sid': i, 'url': 'http://www.dianping.com/shop/' +
               i + '/review_more_latest'}
        res.append(url)
    return n, res


def prepare():
    n, res = get_url()
    print n
    offset = n / 2
    i = 0
    for i in range(offset):
        sendMsg(res[i * 2:(i + 1) * 2])
        print '发送第　%d 组' % i

    if (i * 2 < n):
        sendMsg(res[i * 2:])
    print '结束'


if __name__ == '__main__':
    print 'start ...'
    prepare()
