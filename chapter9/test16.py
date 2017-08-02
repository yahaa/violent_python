# encoding=utf-8
# user station sql 语句生成脚本

import random


name = 'zihua{}'
email = 'yuanzihua@gmail.com'
password = '123456'
phone = '18777859598'
pic = 'default'
role = 'other'
for i in range(1, 10):
    print 'insert into user value ("{}","{}",md5({}),"{}","{}","{}");'.format(name.format(i), email, password, phone, pic, role)

users = []
for i in range(4, 9):
    users.append(name.format(i))
print users

station_sql = 'insert into station VALUES (%d,%s,%s,%.2f,%.2f,%.2f,%.6f,%.6f,%s,%.2f,%.2f,%d,%s,%s,%s);'
city = ("上海", "北京", "深圳", "杭州", "武汉")
for i in range(15):
    print station_sql % (i,
                         "now()",
                         "'" + city[random.randint(0, 4)] + "'",
                         random.uniform(0, 100),
                         random.uniform(0, 100),
                         random.uniform(0, 100),
                         random.uniform(-90, 90),
                         random.uniform(-180, 180),
                         '"{}区"'.format(city[i % 5]),
                         random.uniform(0, 100),
                         random.uniform(0, 100),
                         random.randint(0, 1000),
                         '"station{}"'.format(i),
                         '"default_station"',
                         "'" + users[random.randint(0, 4)] + "'")
