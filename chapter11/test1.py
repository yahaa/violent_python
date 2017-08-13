import datetime
import time
import random
sql = 'insert into day_total_power value({},"{}",{},{});'

t = time.time()
# print type(t)
# print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
# print random.uniform(40, 80)

u = 1
for i in range(1, 1000 * 16):
    t -= 86400
    if i % 1000 == 0:
        t = time.time()
        u += 1
    print sql.format(i, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)),
                     float('%.3f' % random.uniform(4000, 8000)), u)
