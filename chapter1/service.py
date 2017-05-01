import socket
import sys
import argparse

host = 'localhost'


def echo_service(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print 'Server start at :%s :%s' % (host, port)
    print 'Wait for connection ...'
    while True:
        conn, addr = s.accept()
        print 'Connected by', addr
        while True:
            try:
                data = conn.recv(1024)
                print data
                conn.send("server redeived you message.")
            except socket.error, e:
                print e
                break
    # s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store",
                        dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_service(port)
