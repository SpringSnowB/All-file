from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',1234))
s.listen(3)


#创建poll对象
p = epoll()

#建立查找字典
fdmap = {s.fileno():s}

#关注s套接字
p.register(s,POLLIN)

#循环监控IO的发生
while True:
    #提交监控
    events = p.poll()
    for fd,event in events:
        if fd ==s.fileno():
            c,addr = s.accept()
            print("Connect from",addr)
            p.register(c,EPOLLIN|EPOLLERR)
            fdmap[c.fileno()] = c#注意维护字典与register保持一致
            #poll()的返回值不是IO对象，建立字典来解决

        elif event & EPOLLIN:#如果是POLLIN就绪，为真，否则为假
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'ok')
