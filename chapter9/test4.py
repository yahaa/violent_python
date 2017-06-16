# coding=utf-8
import re
import requests
import scrapy
import MySQLdb
import threading

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='XS',
)
cur = conn.cursor()


def get_latest_com(id):
    url = 'http://www.dianping.com/shop/' + id + '/review_more_latest'
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


def get_store_id():
    n = cur.execute('select store_id from dianping')
    ids = cur.fetchmany(n)
    return n, ids


def main():
    n, ids = get_store_id()
    no = 1
    for i in ids:
        i = i[0]
        print '[%d/%d] 正在抓取　%s 号店铺的最新评论' % (no, n, i)
        no += 1
        time = get_latest_com(i)
        sql = 'update dianping set store_latest_com="' + \
            time + '" where store_id="' + i + '"'
        cur.execute(sql)


def main_t():
    n, ids = get_store_id()
    offset = n / 200
    threads = []
    for i in range(offset):
        tids = ids[i * 200:(i + 1) * 200]
        t = threading.Thread(target=main_jod, args=(tids, i + 1,))
        threads.append(t)
    t = threading.Thread(target=main_jod, args=(ids[offset * 200:], offset))
    threads.append(t)

    for item in threads:
        item.setDaemon(True)
        item.start()
    item.join()
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
