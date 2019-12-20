"""
使用进程池备份目录，该目录中包含若干个普通文件
"""
from multiprocessing import Pool
import os

PATH = '/home/tarena/code/m2/d06/'
COPY_PATH = '/home/tarena/备份/'
list_dir = os.listdir(PATH)
copy_size = 0
def copy_file(dir_name):
    file = open(PATH+dir_name,'rb')
    fr = open(COPY_PATH+dir_name,'wb')
    n = fr.write(file.read())
    file.close()
    fr.close()
    calculate(n)
def calculate(n):
    all_size = os.path.getsize(PATH)
    global copy_size
    while n < all_size:
        copy_size += n
        print(copy_size / all_size)


pool = Pool(4)
for dir in list_dir:
    pool.apply_async(func=copy_file,args=(dir,))


pool.close()
pool.join()

