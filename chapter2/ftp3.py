import ftplib


def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
        print dirList
    except:
        dirList = []
        print 'Could not list directory contents'
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn or '.jsp' in fn:
            print 'found default page: ' + fileName
            retList.append(fileName)
    return retList
host = '115.29.146.79'
userName = 'yahaa'
password = '********'
ftp = ftplib.FTP(host)
ftp.login(userName, password)
print returnDefault(ftp)
