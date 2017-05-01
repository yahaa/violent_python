import socket
import sys
import argparse
host = 'localhost'


def echo_client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        cmd = raw_input('Please input msg:')
        s.send(cmd)
        data = s.recv(1024)
        print data
    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client')
    parser.add_argument('--port', action="store",
                        dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
