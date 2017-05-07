# -*- coding: UTF-8 -*-
# 该脚本为hadoop 环境变量配置
import os

path = 'export # HADOOP PATH\n\
export HADOOP_HOME=/home/hadoop/hadoop-2.7.3\n\
export PATH=\$HADOOP_HOME/bin:\$PATH'
option = ['tar -xzvf hadoop-2.7.3.tar.gz',
          'echo "' + path + '" ' + '>> ~/.bashrc', 'source .bashrc ']


for i in option:
    os.system(i)
