from socket import *
sockdf = socket(AF_INET,SOCK_DGRAM)
ADDR_SERVER = ('127.0.0.1',1236)
while True:
    word = input("please input the word you find:")
    if not word:
        break
    sockdf.sendto(word.encode(), ADDR_SERVER)
    msg ,addr = sockdf.recvfrom(1024)
    print("From Server:",msg.decode())
sockdf.close()