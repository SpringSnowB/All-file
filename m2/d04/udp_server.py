from socket import *
sockdf = socket(AF_INET,SOCK_DGRAM)
sockdf.bind(('0.0.0.0',1234))
while True:
    data,addr = sockdf.recvfrom(1024)
    print("Receive from %s:%s"%(addr,data.decode()))
    sockdf.sendto(b'hahahaha',addr)

sockdf.close()
