import socket
import sys
import threading

con = threading.Condition()
host = 'localhost'
port = 7777
data = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Server socket created'
s.bind((host, port))
s.listen(10)
print 'Server started.'


def clientThreadIn(conn, nick):
    global data
    while True:
        try:
            temp = conn.recv(1024)
            if temp == 'leave':
                conn.close()
                return
            notify(temp)
            print data
        except:
            notify(nick + ' leaves the room!')
            print data
            return


def notify(msg):
    global data
    if con.acquire():
        data = msg
        con.notifyAll()
        con.release()


def clientThreadOut(conn, nick):
    global data
    while True:
        if con.acquire():
            con.wait()
            if data:
                try:
                    conn.send(data)
                    con.release()
                except:
                    con.release()
                    return


if __name__ == '__main__':
    while True:
        conn, addr = s.accept()
        print 'Connected with :', addr
        nick = conn.recv(1024)
        notify('welcome ' + nick + 'to the room!')
        print data
        print str((threading.activeCount() + 1) / 2) + ' person(s)'
        conn.send(data)
        threading.Thread(target=clientThreadIn, args=(conn, nick)).start()
        threading.Thread(target=clientThreadOut, args=(conn, nick)).start()
    s.close()
