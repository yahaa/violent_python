import os
hosts = ['master', 'slave1', 'slave2', 'slave3', 'slave4']

for i in hosts:
    #cmd1 = 'scp ~/jdk1.8.tar.gz hadoop@' + i + ':/home/hadoop/jdk1.8.tar.gz'
    #cmd2 = 'scp ~/build_java.py hadoop@' + i + ':/home/hadoop/build_java.py'
    cmd3 = 'scp ~/hadoop-2.7.3.tar.gz hadoop@' + \
        i + ':/home/hadoop/hadoop-2.7.3.tar.gz'
    # os.system(cmd1)
    os.system(cmd3)
    # os.system(cmd)
