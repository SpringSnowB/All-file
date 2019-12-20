from socket import *
from multiprocessing import Process
import signal,hashlib
from dict_database import *


s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',1234))
s.listen(3)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

db = DictDatabase(database = 'dict',
                     user = 'root',
                     password = '123456')


def encryption(passwd):
    hash = hashlib.md5()
    hash.update(passwd.encode())
    return hash.hexdigest()

def login(c,name,passwd):
    passwd = encryption(passwd)
    if not db.search_user(name):
        c.send("该用户不存在，请注册。".encode())
        return
    if not db.search_passwd(name,passwd):
        c.send('密码错误，请重新输入。'.encode())
        return
    c.send(b'ok')

def register(c,name,passwd):
    passwd = encryption(passwd)
    if db.search_user(name):
        c.send('用户名存在，请重新输入。'.encode())
        return
    if not db.insert_user(name,passwd):
        c.send("入库失败，请重新输入。".encode())
        return
    c.send(b'ok')

def search_word(c,name,word):
    result = db.search_word(word)
    db.insert_search(name,word)
    if result:
        info = "%s :%s"%(word,result)
        c.send(info.encode())
        return
    c.send('not find!'.encode())

def search_history(c,name):
    history = db.search_history(name)
    info_=''
    if not history:
        c.send('您暂时没有历史记录。')
        return
    for h in history:
        info = "name:%s  word:%s  time:%s\n"%(name,h[1],h[2])
        info_ +=info
    c.send(info_.encode())

def handle(c):
    db.create_cur()
    while True:
        data = c.recv(1024).decode()
        tmp = data.split(' ')
        if tmp[0] == 'R':
            register(c,tmp[1],tmp[2])
        elif tmp[0] =='L':
            login(c,tmp[1],tmp[2])
        elif tmp[0] =='S':
            search_word(c,tmp[1],tmp[2])
        elif tmp[0] =='SH':
            search_history(c,tmp[1])
        elif tmp[0] =='Q':
            return

def main():
    while True:
        try:
            c,addr = s.accept()
            print('connect from:',addr)
        except KeyboardInterrupt:
            c.send(b"Q")
            db.close()
            break
        except Exception as e:
            print(e)
            continue
        p =Process(target=handle,args=(c,))
        p.daemon = True
        p.start()

if __name__ == '__main__':
    main()