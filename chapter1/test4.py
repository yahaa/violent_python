import socket
import sys


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def main():
    ip = '115.29.146.'
    port = 21
    for i in range(255):
        banner = retBanner(ip + str(i), port)
        if banner:
            print ip + str(i), banner

if __name__ == '__main__':
    main()
