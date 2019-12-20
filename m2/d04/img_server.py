"""
练习 ： 选择一张图片，从客户端上传到服务端

       温馨提示： 客户端读取图片的内容
                 将内容发送给服务端
                 服务端接受图片内容
                 保存在服务端某个位置
"""
from socket import *
from time import strftime
IMG_PATH = '/home/tarena/code/m2/d04/photo/'
sockdf = socket()
sockdf.bind(('0.0.0.0',1234))
sockdf.listen(5)
conndf,addr = sockdf.accept()
print("finish connecting:",addr)

time_str = strftime('%Y-%m-%d-%H-%M-%S')
file = open(IMG_PATH+time_str,'wb')

while True:
    img = conndf.recv(1024)
    if not img:
        break
    file.write(img)
file.close()
conndf.close()
sockdf.close()
