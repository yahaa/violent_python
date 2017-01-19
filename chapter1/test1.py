import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(('115.29.146.79', 21))
    ans = s.recv(1024)
    print ans
except Exception, e:
    print '[-] Error = ' + str(e)
