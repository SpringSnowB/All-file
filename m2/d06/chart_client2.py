from socket import *
import os
import sys

ADDR = ('127.0.0.1',1234)

def enter(sockdf):
    while True:
        name=input("请输入姓名登录：")
        msg = 'L '+name
        sockdf.sendto(msg.encode(),ADDR)
        data ,addr = sockdf.recvfrom(1024)
        print(data.decode())
        return name

def send_msg(sockdf, name):
    while True:
        text = input("Msg:")
        if text == 'quit':
            msg = 'Q '+name
            sockdf.sendto(msg.encode(),ADDR)
            sys.exit("退出群聊")
        msg = "C %s %s"%(name,text)
        sockdf.sendto(msg.encode(),ADDR)

def recv_msg(sockdf):
    while True:
        data ,addr = sockdf.recvfrom(4096)
        print(data.decode())

def main():
    sockdf = socket(AF_INET,SOCK_DGRAM)
    #登录
    name = enter(sockdf)
    #聊天
    pid = os.fork()
    if pid < 0:
        print('ERROR')
    elif pid == 0:
        send_msg(sockdf, name)
    else:
        recv_msg(sockdf)

if __name__ == '__main__':
    main()