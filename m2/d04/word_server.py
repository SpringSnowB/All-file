from socket import *

sockdf = socket(AF_INET,SOCK_DGRAM)
sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#设置端口立即被重用
sockdf.bind(('0.0.0.0',1236))
def find_word(word):
    file = open('/home/tarena/code/m2/d02/dict.txt')
    for line in file:
        w = line.split(" ")[0]
        if w > word:
            return "未找到该单词"
        elif word == w:
            return line
    else:
        return "未找到该单词"

while True:
    word, addr = sockdf.recvfrom(1024)
    print("Receive from %s:%s" % (addr, word.decode()))
    sockdf.sendto(find_word(word.decode()).encode(), addr)

