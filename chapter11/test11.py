# coding=utf-8
import random
import MySQLdb
import sys
import json
import time
reload(sys)
sys.setdefaultencoding('utf-8')

conn = MySQLdb.connect(
    host='115.29.146.79',
    port=3306,
    user='yahaa',
    passwd='Asd147258',
    db='webService',
)
cur = conn.cursor()


def sn():
    n = cur.execute(
        'select sn from weather_meter')
    ids = cur.fetchmany(n)
    return n, ids


def ids(sn):
    n = cur.execute(
        'select id from weather_meter_data where weather_meter_sn="{}"'.format(sn))
    idss = cur.fetchmany(n)
    return n, idss


def csql():
    n, sni = sn()
    t = 0
    for item in sni:
        sn_sql(item[0])
        t += 1


def sn_sql(sn):

    n, idss = ids(sn)
    t = time.time()
    #
    for item in idss:
        print 'update {}'.format(item[0])
        t -= 60 * 5
        tr = time.strftime("%Y-%m-%d %X", time.localtime(t))
        cur.execute(
            'update weather_meter_data set time="{}" where id={}'.format(tr, item[0]))
    conn.commit()


# sn_sql(10)
csql()
