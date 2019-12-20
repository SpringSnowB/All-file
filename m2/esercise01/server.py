"""
1. 编写一组程序，分为客户端和服务端
2. 客户端用于与用户交互，用户可以通过input()选择一个文本文件
（存在大量的括号内容(),[],{},《》，但是这些括号可能存在匹配
不正确的情况），将这个文件发送给服务端
3. 服务端需要判断发过来的文件中括号匹配是否正确，如果正确则
给客户端回复完全正确的信息，如果不正确，需要告知
客户端不正确，并且支出括号不正确的位置
   比如此时客户端会收到： “在地18个字符位置 { 不正确 ”
"""
from socket import *
sockdf = socket(AF_INET,SOCK_DGRAM)
sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockdf.bind(('0.0.0.0',1234))

def find_symbol(addr):
    file = open('./client-'+str(addr))
    data = file.read()
    while True:
        left = data.find('{')
        right = data.find('}')
        location = data.find('{',left,right)
        if location:
            return location
        try:
            data = data.split('}',1)[1]
        except:
            return '{ }没有丢失'

def write_file(data,addr):
    file = open('./client-'+str(addr),'a')
    file.write(data)
    file.close()

def receive_file():
    while True:
        data ,addr = sockdf.recvfrom(1024)
        if not data:
            break
        write_file(data,addr)
    return addr




