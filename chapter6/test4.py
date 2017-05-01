import socket

def machine_info():
    host_name=socket.gethostname()
    ip_address=socket.gethostbyname(host_name)
    print 'Host name:%s' %host_name
    print 'Ip address:%s' %ip_address

if __name__=='__main__':
    machine_info()
