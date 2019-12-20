import os
from time import sleep
pid = os.fork()

def fun01():
    for i in range(3):
        sleep(3)
        print("------------")

def fun02():
    for i in range(4):
        sleep(4)
        print("++++++++++++")

pid1 = os.fork()
if pid1 == 0:
    pid2 = os.fork()
    if pid2 == 0:
        fun02()#二级子进程做fun2
    else:
        os._exit(2)#退出一级子进程
else:
    os.wait()#等pid1退出
    fun01()
