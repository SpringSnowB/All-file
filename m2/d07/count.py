"""
100000内质数和
多进程
"""

from multiprocessing import Process
from esercise import *

class Prime(Process):
    def __init__(self, begin=1, end=100000):
        super().__init__()
        self.begin = begin
        self.end = end

    def run(self):
        count_number(self.begin,self.end)

@print_time
def use_4_process():
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(i,i+25000)
        p.start()
        jobs.append(p)
    for job in jobs:
        job.join()

use_4_process()



# import signal
# signal.signal(signal.SIGCHLD,signal.SIG_IGN)
# p1 = os.fork()
# if p1 == 0:
#     p2 = os.fork()
#     if p2 == 0:
#         r1 = esercise.count_number(1,25000)
#     else:
#         r2 = esercise.count_number(25001,50000)
# else:
#     p3 = os.fork()
#     if p3 == 0:
#         r3 = esercise.count_number(50001, 75000)
#     else:
#         r4 = esercise.count_number(750001,100000)
