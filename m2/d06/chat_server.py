from socket import *
import os
client_dict = {}
ADDR = ('0.0.0.0', 1234)
sensitive_word_list = ['oo','pp']
count_sensitive_dict = {}
force_exit_list = []

def warning(name,sockdf):
    msg = '管理员：%s使用敏感词汇，发出警告'%name
    for v in client_dict.values():
        sockdf.sendto(msg.encode(),v)

def sensitive_word(name,text,sockdf):
    count = 0
    for word in sensitive_word_list:
        if word in text:
            text =text.replace(word,'**')
            count += 1
    if count != 0:
        warning(name,sockdf)
        count_sensitive_dict[name] += 1
    return text


def login(name,addr,sockdf):
    count_sensitive_dict[name] = 0
    if name in client_dict.keys() or addr in force_exit_list:
        sockdf.sendto('fail'.encode(),addr)
    else:
        info = name+'进入聊天室\n'
        sockdf.sendto('ok'.encode(),addr)
        for v in client_dict.values():
            sockdf.sendto(info.encode(),v)
        client_dict[name] = addr

def force_exit(name,sockdf,addr):
    del client_dict[name]
    force_exit_list.append(addr)
    msg = '%s使用敏感词汇超过三次，强制退出群聊'%name
    sockdf.sendto('管理员：您使用敏感词汇超过三次，强制退出群聊'.encode(),addr)
    sockdf.sendto(b'quit',addr)
    for v in client_dict.values():
        sockdf.sendto(msg.encode(),v)

def chart(name,text,sockdf,addr):
    msg= name+'：'+sensitive_word(name,text,sockdf)
    if name in count_sensitive_dict and count_sensitive_dict[name] == 3:
        force_exit(name,sockdf,addr)
        return
    else:
        for v in client_dict.values():
            sockdf.sendto(msg.encode(),v)

def quit(name,sockdf):
    del client_dict[name]
    msg = '%s已退出聊天室\n'%(name)
    for v in client_dict.values():
        sockdf.sendto(msg.encode(),v)



def handle(sockdf):
    while True:
        data ,addr = sockdf.recvfrom(1024)
        tmp = data.decode().split(' ',2)
        if tmp[0] =='L':
            login(tmp[1],addr,sockdf)
        elif tmp[0] == 'C':
            chart(tmp[1],tmp[2],sockdf,addr)
        elif tmp[0] =='Q':
            quit(tmp[1],sockdf)


def main():
    sockdf = socket(AF_INET, SOCK_DGRAM)
    sockdf.bind(ADDR)
    pid = os.fork()
    if pid<0:
        return
    elif pid == 0:
        while True:#子进程处理管理员消息
            text = input("管理员消息：")
            msg = 'C 管理员 '+text
            sockdf.sendto(msg.encode(),ADDR)
    else:
        handle(sockdf)#父进程处理客户端请求

if __name__ == '__main__':
    main()