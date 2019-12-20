from socket import *
import struct
sockdf = socket(AF_INET,SOCK_DGRAM)
sockdf.bind(('127.0.0.1',1234))
sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
st = struct.Struct('6s5sif')
file = open('./student.txt','a')

def unpack(data):
    print(str(st.unpack(data)))
    return st.unpack(data)

while True:
    data ,addr = sockdf.recvfrom(1024)
    print("Receive from ",addr)
    if not data:
        break
    data = unpack(data)
    data_id =data[0].decode()
    data_name = data[1].decode()
    data_age = data[2]
    data_height = data[3]
    data_student = "%s   %s   %d    %d"%(data_id,data_name.split('\0')[0],data_age,data_height)
    file.write(data_student)
    file.write('\n')
    file.flush()
    sockdf.sendto(b'finish',addr)
file.close()
sockdf.close()
