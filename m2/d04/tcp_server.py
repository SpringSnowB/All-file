import socket
#创建tcp套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0',1235))#可以让别人用IP访问，也可以让自己通过本地地址访问
#设置监听
sockfd.listen(9)
#处理客户端连接
while True:
    print("Waiting for connect...")
    connfd,addr = sockfd.accept()
    print("finish",addr)
    #收发消息
    while True:
        data = connfd.recv(6).decode()
        #if data =='##':#客户端结束，recv返回  报错BrokenPipeError: [Errno 32] Broken pipe
        if not data:
            break
        print("Recv:",data)
        connfd.send(b"Hello\n")#必须是字节串，否则报错
    connfd.close()
sockfd.close()
#关闭套接字
