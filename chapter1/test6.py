import zipfile
try:
    zFile = zipfile.ZipFile("pass.zip")
    zFile.extractall(pwd='12')
except Exception, e:
    print e
