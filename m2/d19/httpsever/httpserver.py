"""
httpserver部分主程序
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
from socket import *
from threading import Thread
from config import *
import re
import json


# 与后端应用交互
def connect_frame(env):
    """
    将请求发送给WebFrame
    从WebFrame接收反馈数据
    """
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except Exception as e:
        print(e)
        return
    # 发送json请求
    data = json.dumps(env)
    s.send(data.encode())
    # 获取返回的数据 (json格式)
    data = s.recv(1024 * 1024 * 10).decode()
    if data:
        return json.loads(data)  # 返回字典


# 主体功能写入类
class HTTPServer:
    def __init__(self):
        self.address = (HOST, PORT)
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sock = socket()
        self.sock.setsockopt(SOL_SOCKET,
                             SO_REUSEADDR,
                             DEBUG)

    # 绑定地址
    def bind(self):
        # 有些属性可以在调用函数时再生产
        self.host = HOST
        self.port = PORT
        self.sock.bind(self.address)

    # 服务启动函数 (多线程并发)
    def serve_forever(self):
        self.sock.listen(3)
        print("Listen the port %d" % self.port)
        while True:
            connfd, addr = self.sock.accept()
            print("Connect from", addr)
            t = Thread(target=self.handle,
                       args=(connfd,))
            t.setDaemon(True)
            t.start()

    # 处理具体的浏览器请求
    def handle(self, connfd):
        # http请求
        request = connfd.recv(4096).decode()
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            # 与webframe交互 (数据字典/None)
            data = connect_frame(env)
            if data:
                self.response(connfd, data)

    # 组织响应格式
    def response(self, connfd, data):
        # data->{'status':'200','data':'zzzz'}
        if data['status'] == '200':
            res="HTTP/1.1 200 OK\r\n"
            res+="Content-Type:text/html\r\n"
            res+="\r\n"
            res+=data['data']
        elif data['status'] == '404':
            res="HTTP/1.1 404 Not Found\r\n"
            res+="Content-Type:text/html\r\n"
            res+="\r\n"
            res+=data['data']
        connfd.send(res.encode()) # 响应给浏览器


if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.serve_forever()  # 启动服务
