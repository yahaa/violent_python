# -*- coding: UTF-8 -*-
# 测试用
import os
hosts = ['master', 'slave1']
for i in hosts:
    cmd = 'ssh hadoop@' + i
    os.system(cmd)
    os.system('ls')
    os.system('exit')
