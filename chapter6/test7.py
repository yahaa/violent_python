import socket


def get_remote_info(host_name):
    try:
        print socket.gethostbyname(host_name)
    except socket.error, err_msg:
        print '%s:%s' % (host_name, err_msg)
if __name__ == '__main__':
    get_remote_info('www.baidu.com')
