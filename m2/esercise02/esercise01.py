"""
写两个线程，一个线程打印1-52,另一个线程打印A-Z，
要求打印顺序为12A34B56C...5152Z，
不能使用sleep进行时间控制
"""
from  threading import Thread,Lock

lock1  = Lock()
lock2  = Lock()

count = 1
def print_number():
    for item in range(1,52,2):
        lock1.acquire()
        print(item,end=' ')
        print(item+1,end=' ')
        lock2.release()


def print_word():
    for item in range(ord('A'),ord('Z')+1):
        lock2.acquire()
        print(chr(item),end=' ')
        lock1.release()

t1 = Thread(target=print_number)
t2 = Thread(target=print_word)
lock2.acquire()
t1.start()
t2.start()
t1.join()
t2.join()





