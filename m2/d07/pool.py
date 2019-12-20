from multiprocessing import Pool
from time import sleep,ctime

#进程池事件函数

def worker(msg):
    sleep(2)
    print(ctime(),'--',msg)

#创建进程池
pool = Pool(3)

#向进程池中放入事件
for i in range(10):
    msg = "action %d"%i
    r =pool.apply_async(func=worker,args=(msg,))

#关闭进程池
pool.close()
#回收进程池
pool.join()
print(r.get())#获取进程池事件函数的返回值