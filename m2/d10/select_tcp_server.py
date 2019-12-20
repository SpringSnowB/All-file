from socket import *
from select import select

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',1234))
s.listen(3)

#设置关注的IO
rlist = [s]  #s的读IO行为
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rlist:
        if r is s:#有新的客户端连接
            c, addr = rs[0].accept()
            print("Connect from:", addr)  # 端口重用，上一个连接会被覆盖，强制退出
            rlist.append(c)
        else:#某个客户端发送消息
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
            print(data)
            # r.send(b'ok')
            wlist.append(r)
    for w in wlist:
        w.send(b'ok')
        wlist.remove(w)

