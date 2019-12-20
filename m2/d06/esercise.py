"""
一个文件，分别复制文件的上半部分和后半部分，形成两个新的文件
"""
from multiprocessing import Process
import os
path = './u.txt'
size = os.path.getsize(path)

def top():
    fr = open(path,'rb')
    fw = open('./copy-top.txt','wb')
    fw.write(fr.read(size//2))
    fr.close()
    fw.close()

def botton():
    fr = open(path,'rb')
    fw = open('./copy-bot.txt','wb')
    fr.seek(size//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()

p1 = Process(target=top)
p2 =Process(target=botton)
p1.start()
p2.start()
p1.close()
p2.close()

