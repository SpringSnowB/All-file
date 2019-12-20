"""
多线程
"""
from threading import Thread
from socket import *
import signal
from multiprocessing import Process
import os

HOST = '0.0.0.0'
POST = 1234
ADDR = (HOST,POST)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(7)
#signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def handle(conndf,addr):
    while True:
        recrive = conndf.recv(6)
        if recrive == b'##':
            print("exit:", addr)
            break
        conndf.send(b'hello')
        print(addr,":",recrive)
    conndf.close()

while True:
    try:
        conndf, addr = s.accept()
        print('Connect from', addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    t = Thread(target=handle,args=(conndf,addr))
    t.setDaemon(True)#主线程退出，分支线程也退出
    t.start()

    # p = Process(target=handle,args=(conndf,addr))
    # p.daemon = True
    # p.start()  #多进程，用single处理

