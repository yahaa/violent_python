# -*- coding: UTF-8 -*-
# 该脚本主要用于本地和集群间数据传送用的
import os
hosts = ['master', 'slave1', 'slave2', 'slave3', 'slave4', 'slave5']

for i in hosts:

    cmd2 = 'scp ~/build_env.py hadoop@' + i + ':/home/hadoop/build_env.py'
    os.system(cmd2)
    # cmd4 = 'scp ~/build_hadoop.py hadoop@' + \
    #     i + ':/home/hadoop/build_hadoop.py'
    # os.system(cmd4)
    # os.system(cmd)


# 只需要复制一份数据到主节点
# m = 'scp ~/hadoop-2.7.3.tar.gz hadoop@master:/home/hadoop/hadoop-2.7.3.tar.gz'
# os.system(m)
#cmd1 = 'scp ~/jdk1.8.tar.gz hadoop@' + i + ':/home/hadoop/jdk1.8.tar.gz'
# os.system(cmd1)
