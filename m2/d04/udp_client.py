from socket import *
sockdf = socket(AF_INET,SOCK_DGRAM)
ADDR_SERVER = ('127.0.0.1',1234)
while True:
    data = input("Mag:")
    if not data:
        break
    sockdf.sendto(data.encode(),ADDR_SERVER)
    msg ,addr = sockdf.recvfrom(1024)
    print("From Server:",msg.decode())
sockdf.close()