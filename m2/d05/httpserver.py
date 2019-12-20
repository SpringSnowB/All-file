from socket import *

def handle(conndf):
    request = conndf.recv(4096).decode()
    if not request:
        return
    request_line = request.split('\n')[0]
    request_info = request_line.split(' ')[1]

    if request_info =='/':
        response = 'HTTP/1.1 200 OK\r\n'
        response +='Content-Type:text/html;charset=UTF-8\r\n'
        response +='\r\n'
        with open('html.html') as f:
            response += f.read()
    else:
        response = 'HTTP/1.1 404 not found\r\n'
        response += 'Content-Type:text/html;charset=UTF-8\r\n'
        response += '\r\n'
        response += 'Life is short so that I use Python...'
    conndf.send(response.encode())

def main(post):
    sockdf = socket()
    sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockdf.bind(('0.0.0.0',post))
    sockdf.listen(5)
    while True:
        try:
            conndf,addr = sockdf.accept()
        except  KeyboardInterrupt:
            break
        print("connect:",addr)
        handle(conndf)
        conndf.close()
    sockdf.close()

if __name__=='__main__':
    main(1234)