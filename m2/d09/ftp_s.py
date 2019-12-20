from socket import *
import sys,os,time
from threading import Thread

ADDR = ('0.0.0.0',1234)
PATH = './file/'#文件存储位置

class FTPServer(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    def download_file(self):
        pass

    def upload_file(self):
        pass

    def display_file(self):
        pass

    def run(self):
        while True:
            num = self.connfd.revc(6).decode()
            if not num or num ==b'4':
                return
            elif num ==b'1':
                self.display_file()
            elif num ==b'2':
                self.download_file()
            elif num == b'3':
                self.upload_file()
            else:
                return



def main():
    sockdf = socket()
    sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockdf.bind(ADDR)
    sockdf.listen(3)
    print("Waiting for connect...")
    while True:
        try:
            c,addr = sockdf.accept()
            print('Connect from',addr)
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
    t = FTPServer(c)
    t.setDaemon(True)
    t.start()
