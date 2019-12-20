from socket import *
sockdf = socket(AF_INET,SOCK_DGRAM)
ADDR = ('127.0.0.1',1234)
file = open('./file')
while True:
    data = file.read(1024)
    if not data:
        break
    sockdf.sendto(data.encode(),ADDR)
print("发送完毕")
mag,addr = sockdf.recvfrom(1024)
print(mag)
sockdf.close()
file.close()