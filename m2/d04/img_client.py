from socket import *
sockdf = socket()
sockdf.connect(('127.0.0.1',1234))
file = open(input("请收入图片路径："),'rb')
while True:
    img = file.read(1024)
    if not img:
        break
    sockdf.send(img)
file.close()
sockdf.close()