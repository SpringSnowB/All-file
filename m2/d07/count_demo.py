import time
from multiprocessing import Process

def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("%s运行时间%.6f"%(f.__name__,end_time-start_time))
        return  res
    return wrapper

# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

@timeis
def no_multi_process():
    prime = []
    for i in range(1,100001):
        if isPrime(i):
            prime.append(i)
    sum(prime)

class Prime(Process):
    def __init__(self,prime,begin,end):
        super().__init__()
        self.prime = prime  # 装质数的列表
        self.begin = begin # 开始数值
        self.end = end  # 结束数值
    def run(self):
        for i in range(self.begin,self.end):
            if isPrime(i):
                self.prime.append(i)
            sum(self.prime)

@timeis
def use_4_process():
    prime = []
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(prime,i,i+25000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

@timeis
def use_10_process():
    prime = []
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(prime,i,i+10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

if __name__ == '__main__':
    # no_multi_process运行时间26.246834
    # no_multi_process()

    # use_4_process运行时间14.909750
    # use_4_process()

    # use_10_process运行时间13.656211
    use_10_process()