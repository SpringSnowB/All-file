from socket import *
import sys
import getpass


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.connect(('127.0.0.1', 1234))

def primary_interface():
    """
    选择登录或者注册

    """
    while True:
        select = input("""
    —————————————————————
        1    |   注册   
    —————————————————————
        2    |   登录
    ——————————————————————
        3    |   退出
    ——————————————————————""")
        if select =='1':
            register()
        elif select =='2':
            login()
        elif select =='3':
            sys.exit("谢谢使用！")
        else:
            print("请正确输入！")



def advanced_interface(name):
    print("欢迎使用英语词典！")
    while True:

        select = input("""
        —————————————————————
            1    |   查单词   
        —————————————————————
            2    |   历史记录
        ——————————————————————
            3    |   注销
        ——————————————————————
        """)
        if select == '1':
            search_word(name)
        elif select == '2':
            search_history(name)
        elif select == '3':
            primary_interface()
        else:
            print("请正确输入！")


def login():
    name = input("name:")
    passwd = getpass.getpass("password:")
    info = 'L '+name+' '+passwd
    s.send(info.encode())
    receive = s.recv(24)
    if receive==b'ok':
        print("登录成功")
        advanced_interface(name)
    elif receive ==b'Q':
        sys.exit("谢谢使用")
    else:
        print(receive.decode())


def register():
    while True:
        name = input("name:")
        passwd = getpass.getpass("password:")
        repasswd = getpass.getpass("password again:")
        if repasswd != passwd:
            print("两次输入密码不一致")
            continue
        if (' ' in name) or (' ' in passwd):
            print("用户名和密码中村存在空格，请重新输入！")
            continue
        info = "R "+name+" "+passwd
        s.send(info.encode())
        receive = s.recv(128).decode()
        if receive =='ok':
            print("注册成功")
            primary_interface()
        elif receive == b'Q':
            sys.exit("谢谢使用")
        else:
            print(receive)
        return

def search_word(name):
    while True:
        word = input("请输入你要查找的单词：")
        if word =='Q':
            s.send(b'Q ')
            break
        info = "S "+name+' '+word
        s.send(info.encode())
        receive = s.recv(1024)
        if receive ==b'Q':
            sys.exit("谢谢使用")
        print(receive.decode())

def search_history(name):
    info = "SH "+name
    s.send(info.encode())
    receive = s.recv(1024)
    if receive ==b'Q':
        sys.exit("谢谢使用")
    print(receive.decode())


def main():
    primary_interface()


if __name__ == '__main__':
    main()