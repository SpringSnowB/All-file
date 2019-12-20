"""
一个目录，在目录下有若干个文件（有子目录和普通文件）。
编程将该目录下的普通文件复制到
家目录下的'备份'这个目录中。
"""
import os
path = "/home/tarena/code/m2/d03/"
list_catalogue = os.listdir(path)
# print(list_catalogue)
for file in list_catalogue:
    path_catclogue = path+file
    # print(os.path.isfile(path_catclogue))
    if os.path.isfile(path_catclogue):
        is_file = open(path_catclogue)
        data = is_file.read()
        file_copy = open('/home/tarena/备份/'+file,'w')
        file_copy.write(data)
