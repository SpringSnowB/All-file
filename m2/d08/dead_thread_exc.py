"""
使用多个线程，同时从多个地方拷贝文件的某一部分
最终在本地合并为一个
提示: 1. 判断那些目录下有目标文件
     2. 有几个路径下有，就创建几个线程
     3. 每个线程负责一个路径，要选好下载文件的哪部分
     4. 多个线程下载的内容需要最后为一个文件
"""
import os
from threading import Thread,Lock

urls=[ "/home/tarena/桌面/",
    "/home/tarena/模板/",
    "/home/tarena/音乐/",
    "/home/tarena/图片/",
    "/home/tarena/下载/",
    "/home/tarena/视频/",
]
lock = Lock()
file_copy = open('./copy.jpg', 'wb')

def find_file(file):
    return [item+file for item in urls if os.path.exists(item+file)]

def creat_thread(file):
    exit_file = find_file(file)
    if len(exit_file)== 0:
        os._exit(0)
    number = 0
    jobs = []
    for path in exit_file:
        t = Thread(target=load,args=(path,number))
        jobs.append(t)
        t.start()
        number += 1
    [job.join() for job in jobs]


def load(path,number):
    file = open(path,'rb')
    file_size = os.path.getsize(path)
    with lock:
        file_copy.seek(file_size*number)
        file_copy.write(file.read())
    file.close()

creat_thread('小黑.jpg')
file_copy.close()

