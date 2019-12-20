"""
基于fork的多进程服务
"""
from socket import *
import os
import signal

HOST = '0.0.0.0'
POST = 1234
ADDR = (HOST,POST)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(7)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def handle(conndf):
    while True:
        recrive = conndf.recv(6)
        if recrive ==b'##':
            break
        conndf.send(b'hello')
        print(recrive)
    conndf.close()


while True:
    try:
        conndf,addr = s.accept()
        print('Connect from',addr)
    except KeyboardInterrupt:
        os._exit(1)
    except Exception as e:
        print(e)
        continue

    pid = os.fork()
    if pid == 0:
        handle(conndf)
        print("exit",addr)
        conndf.close()
        s.close()
        os._exit(0)
    else:
        continue






