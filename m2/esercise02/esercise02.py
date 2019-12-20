"""
模拟生产,入库,销售场景
假定企业自产，自存，自销。将工厂生产的产品不定时的运到仓库，与此同时，仓库货物需要运到商场销售。
请编写一个程序模拟这个过程，（主要是对仓库的存取）。

* 仓库可存量，可以设置为一个常量，比如max = 10
* 仓库满的时候不能向仓库存入货物
* 仓库空的时候不能向商场提供货物
* 写多线程表达货物的存储和提取，而这两个操作是同时进行的
* 不能出现先存满再取完或者先取完再存满的情况
"""
from threading import Thread
import time
from random import randint

MAX_STORAGE = 100
ware = []

def produce(name):
    count = 0
    while True:
        print(name,'producing...')
        time.sleep(2)
        if len(ware)>= 10:
            print('ware is full...')
            time.sleep(2)
        else:
            ware.append('good_%d'%count)
            print('%d good produced...'%count)
            count += 1

def consumer(name):
    while True:
        time.sleep(randint(1,8))
        if len(ware) <= 0:
            print('no goods...')
            time.sleep(4)
        else:
            print('consumer %s bought %s'%(name,ware.pop(0)))


p1 = Thread(target=produce,args=('spring',))
c1 = Thread(target=consumer,args=('玉石',))
c2 = Thread(target=consumer,args=('玉珏',))
c3 = Thread(target=consumer,args=('玉枕',))

p1.start()
c1.start()
c2.start()
c3.start()

p1.join()
c1.join()
c2.join()
c3.join()