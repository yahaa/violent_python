import socket
import threading

inString = ''
outString = ''
nick = ''


def dealOut(s):
    global nick, outString
    while True:
        outString = raw_input()
        outString = nick + ': ' + outString
        s.send(outString)


def dealIn(s):
    global inString
    while True:
        try:
            inString = s.recv(1024)
            if not inString:
                break
            if outString != inString:
                print inString
        except:
            break


nick = raw_input('Input your nickName:')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 7777))
sock.send(nick)
thin = threading.Thread(target=dealIn, args=(sock,)).start()
thout = threading.Thread(target=dealOut, args=(sock,)).start()
