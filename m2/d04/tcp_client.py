from socket import *

sockfd = socket()
#连接诶服务器
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.connect(('127.0.0.1',1234))
while True:
    data = input("msg:")
    if data == '##':
        sockfd.send(data.encode())
        break
    sockfd.send(data.encode())
    reveive = sockfd.recv(6)
    print("Server:",reveive.decode())

sockfd.close()