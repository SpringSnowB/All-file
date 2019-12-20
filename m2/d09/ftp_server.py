"""
自定义线程类

"""
import os
from socket import *
from multiprocessing import Process
import signal
from time import sleep

PATH = './file/'

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',1234))
s.listen(3)
print("欢迎进入")
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def display_file(conndf):
    list_file = os.listdir(PATH)
    if not list_file:
        conndf.send('文件库为空'.encode())
        sleep(0.01)
        return
    else:
        conndf.send(b'ok')
        files = '\n'.join(list_file)
        conndf.send(files.encode())




def download_file(c):
    file_name = c.recv(64).decode()
    if file_name in os.listdir(PATH):
        c.send('文件存在，可以下载'.encode())
        sleep(0.01)
        file = open(PATH+file_name,'rb')
        while True:
            fr = file.read(1024)
            if not fr:
                break
            c.send(fr)
        print("下载完毕")
        file.close()
    else:
        c.send(b'sorry,not find')
    # c.close()

def upload_file(conndf):
    file = conndf.recv(10)
    path = PATH+file.decode()
    if os.path.exists(path):
        conndf.send(b'sorry,not find')
    else:
        send_file = open(path)
        while True:
            fr = send_file.read(1024)
            if not fr:
                break
            conndf.send(fr)
        send_file.close()


def exit_system(conndf):
    conndf.send('谢谢使用'.encode())
    conndf.close()

def select_num(c):
    while True:
        num = c.recv(4)
        if num ==b'1':
            display_file(c)
        elif num ==b'2':
            download_file(c)
        elif num ==b'3':
            upload_file(c)
        else:
            exit_system(conndf)
            return


while True:
    try:
        conndf, addr = s.accept()
        print('Connect from', addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    select_num(conndf)
    # conndf.close()