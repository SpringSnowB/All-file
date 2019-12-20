"""
 写一个程序，实现对一个文件进行拷贝

       * input() 输入一个文件位置
       * 将该文件'拷贝'到主目录下
       * 文件可能是文本文件也可能是二进制文件
       * 文件可能比较大，不允许一次性读取

       温馨提示： 从源文件读取内容，写入到目标新文件中

"""
file_open = open(input("请输入文件位置："))#/home/tarena/code/m2/d02/dict.txt
file_write = open('/home/tarena/file_write.txt','wb')
while True:
    file_read = file_open.read(100)
    if not file_read:
        break
    file_write.write(file_read.encode())
file_open.close()
file_write.close()
