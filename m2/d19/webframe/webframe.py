"""
webframe  模拟网站应用做数据处理

从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""
from socket import *
from setting import *
from threading import Thread
import json,os

# 应用类
class Application:
    def __init__(self):
        self.addr=(HOST,PORT)
        self.dir =DIR
        self.create_sock()
        self.bind()

    def create_sock(self):
        self.sock =socket()
        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    def bind(self):
        self.host = HOST
        self.port = PORT
        self.sock.bind(self.addr)

    def find_html(self, info):
        file_list = os.listdir(self.dir)
        if info in file_list:
            return True
        return False

    def get_html(self,info):
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type:text/html;charset=UTF-8\r\n'
        response += '\r\n'
        if info == '/':
            f = open(self.dir + 'index.html')
            response += f.read()
            f.close()
        else:
            if self.find_html(info):
                f = open(self.dir + info)
                response += f.read()
                f.close()
            else:
                response += 'Sorry, 404 NOT FOUND'
        return response

    def get_data(self):
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type:text/html;charset=UTF-8\r\n'
        response += '\r\n'
        response += 'Sorry,can not find'
        return response

    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        if request['info'] =='/' or request['info'][-5:]=='.html':
            response = self.get_html(request['info'])
        else:
            response =self.get_data()
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()


    def start(self):
        self.sock.listen(3)
        print("Running web frame %d" % self.port)
        while True:
            connfd, addr = self.sock.accept()
            print("Connect from", addr)
            t = Thread(target=self.handle,
                       args=(connfd,))
            t.setDaemon(True)
            t.start()

if __name__ == '__main__':
    app = Application()
    app.start() # 启动应用