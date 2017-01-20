import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('yahaa', 'Asd147258')
        print str(hostname) + ' anonymous login succeeded'
        ftp.quit()
        return True
    except Exception, e:
        print str(hostname) + ' faild login'
        return False
host = '115.29.146.79'
anonLogin(host)
