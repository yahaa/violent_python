import socket
import argparse
from threading import Thread

clients = []


def sendCmd(cmd):
    print 'send cmd ...'
    for sock in clients:
        sock.send(cmd.encode('utf-8'))


def waitConnect(s):
    while True:
        sock, addr = s.accept()
        if sock not in clients:
            clients.append(sock)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 7777))
    s.listen(1024)
    t = Thread(target=waitConnect, args=(s,))
    t.start()

    while not len(clients):
        pass
    while True:
        print '#-H xxx.xxx.xxx.xxx -P xxx -C <...>'
        cmd = raw_input('>>> ')
        print cmd
        if len(cmd):
            if cmd[0] == '#':
                sendCmd(cmd)
            elif cmd[0] == '*':
                sys.exit(0)


if __name__ == '__main__':
    main()
