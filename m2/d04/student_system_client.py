from socket import *
import struct
sockdf = socket(AF_INET,SOCK_DGRAM)
st =  struct.Struct('6s5sif')
ADDR_SERVER = ('127.0.0.1',1234)
sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

def get_student():
    id = input("请输入id：")
    if id == '':
        return False
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    height = float(input("请输入身高："))
    return (id.encode(),name.encode(),age,height)

def package(data):
    return st.pack(*data)

while True:
    data = get_student()
    if not data:
        break
    sockdf.sendto(package(data),ADDR_SERVER)
    msg,addr = sockdf.recvfrom(1024)
    print(msg.decode())

sockdf.close()
