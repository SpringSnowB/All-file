from multiprocessing import Process
from time import sleep,ctime

class MyProcess(Process):
    def __init__(self, value=0):
        self.value = value
        super().__init__()

    def f1(self):
        sleep(0.8)
        print(1)

    def f2(self):
        sleep(1)
        print(2)

    def run(self):
        for i in range(self.value):
            self.f1()
            self.f2()
p = MyProcess(3)
p.start()#创建进程  会自动调用run方法
p.join()#回收进程