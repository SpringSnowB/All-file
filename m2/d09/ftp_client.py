from socket import *
sockdf = socket()
sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockdf.connect(('127.0.0.1',1234))

def select_num():
    return input("""
    |  1  |  查看文件  |
    |  2  |  下载文件  |
    |  3  |  上传文件  |
    |  4  |  退出系统  |
    请选择：
    """)

def display_file(sockdf):
    receive = sockdf.recv(128)
    print(receive.decode()+'\n')
    if receive == b'ok':
        files = sockdf.recv(128).decode()
        print(files)
    else:
        return


def download_file(sockdf):
    file_name = input("请输入要下载的文件名：")
    sockdf.send(file_name.encode())
    certain = sockdf.recv(64).decode()
    print(certain,end='\n')
    if certain =='sorry,not find':
        return
    file = open('./file_load/'+file_name,'wb')
    while True:
        file_line = sockdf.recv(1024)
        if not file_line:
            print("下载完毕")
            file.flush()
            break
        file.write(file_line)
    file.close()

def upload_file(sockdf):
    pass

def exit(sockdf):
    print(sockdf.recv(128).decode())
    sockdf.close()


while True:
    num = select_num()
    sockdf.send(num.encode())
    if num == '4':
        break
    elif num == '1':
        display_file(sockdf)
    elif num == '2':
        download_file(sockdf)
    elif num == '3':
        upload_file(sockdf)




