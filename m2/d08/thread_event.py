"""
thread_event 互斥方法演示
"""
from threading import Thread,Event

s = None #用于通信，共享资源
e = Event()
def yangzirong():
    print("yangzirong")
    global s
    s = '天王盖地虎'
    e.set() #解除阻塞

t = Thread(target=yangzirong)

t.start()
print("说口令")
e.wait() #阻塞
if s =='天王盖地虎':
    print("宝塔镇河妖")
else:
    print("dead")

t.join()
