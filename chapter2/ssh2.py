import pexpect
from pexpect import pxssh


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before


def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print '[-] Error connecting'
        exit(0)


def main():
    host = '115.29.146.79'
    user = 'yahaa'
    password = '*********'
    s = connect(host, user, password)
    send_command(s, 'pwd')

if __name__ == '__main__':
    main()
