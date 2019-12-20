from socket import *
from select import select
import os

class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8080,dir='./static'):
        self.host = host
        self.port = port
        self.dir = dir+'/'
        self.addr = (host,port)
        self.rlist = []
        self.wlist = []
        self.xlist = []
        #直接创建套接字
        self.create_socket()

    #创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.addr)

    def handle(self,c):
        request = c.recv(4096).decode()
        #防止客户端断开
        if not request:
            self.rlist.remove(c)
            c.close()
            return
        request_line = request.split('\n')[0]
        info = request_line.split(' ')[1]
        print(c.getpeername,':',info)#打印请求内容

        #根据请求内容，将其分为两类
        if info =='/' or info[-5:]=='.html':
            self.get_html(c,info)
        else:
            self.get_data(c)
        c.close()
        self.rlist.remove(c)

    def get_html(self,c,info):
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type:text/html;charset=UTF-8\r\n'
        response += '\r\n'
        if info =='/':
            f = open(self.dir+'index.html')
            response +=f.read()
            f.close()
        else:
            if self.find_html(info):
                f = open(self.dir+info)
                response += f.read()
                f.close()
            else:
                response += 'Sorry, 404 NOT FOUND'
        c.send(response.encode())
        c.close()

    def find_html(self,info):
        file_list = os.listdir(self.dir)
        if info.split('/')[1] in file_list:
            return True
        return False

    def get_data(self,c):
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type:text/html;charset=UTF-8\r\n'
        response += '\r\n'
        response +='Sorry,can not find'
        c.send(response.encode())
        c.close()

    #启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d"%self.port)
        #IO多路复用方法监控IO
        self.rlist.append(self.sockfd)
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    #浏览器连接
                    c,addr = r.accept()
                    self.rlist.append(c)
                else:
                    #处理具体请求
                    self.handle(r)

if __name__ == '__main__':
    #通过HTTPServer类快速搭建服务
    #通过该服务让浏览器访问到我的网页
    #1.使用流程
    #2.需要用户确定的内容

    HOST = '0.0.0.0'
    PORT = 8000
    DIR = './static'
    httpd = HTTPServer(HOST,PORT,DIR)#生成对象
    httpd.serve_forever()#启动服务
