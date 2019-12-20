"""
实时写入当前时间按
每次写入占一行
可以实时查看写入内容
当程序重新启动后，书写内容能够衔接之前的序号内容
"""
import time
class WriteTime:
    def __init__(self):
        self.__id = 0
        self.__file = open('file1', 'r+')
    def __get_time(self):
        return time.strftime(". %Y-%m-%d   %H:%M:%S\n")

    def __find_id(self):
        try:
            self.__id = int(self.__file.readlines()[-1].split('.')[0])
        except IndexError:
            self.__id = 0

    def __count_id(self):
        self.__id +=1

    def write_time(self):
        self.__find_id()
        while True:
            self.__count_id()
            time_write = str(self.__id)+self.__get_time()
            self.__file.write(time_write)
            print(time_write)
            time.sleep(2)
            self.__file.flush()


time_write = WriteTime()
time_write.write_time()
