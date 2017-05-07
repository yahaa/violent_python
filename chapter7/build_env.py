# -*- coding: UTF-8 -*-
# 该脚本为配置java环境以及hadoop环境用
import os

path = '# JDK PATH\n\
export JAVA_HOME=/home/hadoop/jdk1.8\n\
export JRE_HOME=/home/hadoop/jdk1.8/jre\n\
export CLASSPATH=.:\$JAVA_HOME/lib:\$JRE_HOME/lib:\$CLASSPATH\n\
export PATH=\$JAVA_HOME/bin:\$JRE_HOME/bin:\$PATH\n\
export # HADOOP PATH\n\
export HADOOP_HOME=/home/hadoop/hadoop-2.7.3\n\
export PATH=\$HADOOP_HOME/bin:\$PATH'
option = ['tar -xzvf jdk1.8.tar.gz', 'mv jdk1.8.0_65 jdk1.8', 'tar -xzvf hadoop-2.7.3.tar.gz',
          'echo "' + path + '" ' + '>> ~/.bashrc', 'source .bashrc ']


for i in option:
    os.system(i)
