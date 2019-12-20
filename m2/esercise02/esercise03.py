"""
模拟窗口卖票
有10个窗口（w1...w10）,同时开放售票，一共有50张票（T1--T50），需要按照顺序出售
要求： 输出每一张票的出售时间和窗口，不能出现票未出售或者出售多次的情况。窗口开放之前票存在容器中

1. 使用多线程的同步互斥方法解决问题输出结果
2. 每个线程模拟售票情景
3. 将票的存储提前定一个合理的结构
"""
from threading import Thread,Lock
from time import strftime,sleep

lock = Lock()
ticket = ['T'+str(i) for i in range(1,51)]
def sale_ticket(windown):
    while True:
        if len(ticket) > 0:
            with lock:
                now = strftime("%Y-%m-%d %H:%M:%S")
                print("% s在 %s 卖出了%s" % (windown, now, ticket.pop(0)))
            sleep(0.1)
        else:
            print(windown,"票已售完")
            return
jobs = []

for i in range(1,11):
    windown = '窗口'+str(i)
    t = Thread(target=sale_ticket,args=(windown,))
    t.start()
    jobs.append(t)


[job.join() for job in jobs]

