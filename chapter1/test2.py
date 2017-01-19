import socket


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
    ip1 = '115.29.146.79'
    ip2 = '115.29.146.78'
    port = 21
    banner = retBanner(ip1, port)
    if banner:
        print ip1, banner
    banner2 = retBanner(ip2, port)
    if banner2:
        print ip2, banner2

if __name__ == '__main__':
    main()
