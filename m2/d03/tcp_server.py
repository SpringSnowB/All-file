import socket
#创建tcp套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0',1234))#可以让别人用IP访问，也可以让自己通过本地地址访问
#设置监听
sockfd.listen(9)
#处理客户端连接
print("Waiting for connect...")
connfd,addr = sockfd.accept()
print("finish",addr)
#收发消息
data = connfd.recv(1024)
print("Recv:",data)
n = connfd.send(b"Hello\n")#必须是字节串，否则报错

#关闭套接字
connfd.close()
sockfd.close()