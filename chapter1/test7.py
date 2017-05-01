# encoding=utf-8
import socket


def machine_info():
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    print "Host name: %s" % host_name
    print "IP address: %s" % ip


def remote_machine_info(host_name):
    try:
        print "IP address of %s: %s" % (host_name, socket.gethostbyname(host_name))
    except socket.error, err_msg:
        print "%s: %s" % (host_name, err_msg)


def convert_ipv4(ipv4):
    print "%s ---> %s" % (ipv4, socket.inet_aton(ipv4))


def find_service_name(port):
    print "Port:%s ====> service name: %s" % (port, socket.getservbyport(port))


if __name__ == '__main__':
    remote_machine_info('www.baidu.com')
    remote_machine_info('www.google.com')
    convert_ipv4('115.29.146.79')
    find_service_name(8080)
