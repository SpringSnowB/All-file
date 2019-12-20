from socket import *
sockdf = socket()
sockdf.bind(('0.0.0.0',1234))
sockdf.listen(5)
conndf,addr = sockdf.accept()
print("connect:",addr)
request = conndf.recv(4096).decode()
print(request)
response = """HTTP/1.1 200 OK
Content-Type:text/html;charset=UTF-8

Life is short so that I use Python...

"""
conndf.send(response.encode())
conndf.close()
sockdf.close()