"""
死锁
"""

from time import sleep
from threading import Thread,Lock

#账户类
class Account:
    def __init__(self,id_,balance,lock):
        self.__id = id_
        self.balance = balance
        self.lock = lock

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance +=amount

    def get_balance(self):
        return self.balance



Tom = Account('Tom',5000,Lock())
Alex = Account('Alex',8000,Lock())


def transfer(from_,to,amount):
    from_.lock.acquire()
    from_.withdraw(amount)
    sleep(0.01)
    from_.lock.release()#转完账之后立即释放，就不会造成死锁
    to.lock.acquire()
    to.deposit(amount)
    to.lock.release()


t1 = Thread(target=transfer,args=(Tom,Alex,1500,))
t2= Thread(target=transfer,args=(Alex,Tom,3000,))
t1.start()
t2.start()
t1.join()
t2.join()

print("Tom:",Tom.get_balance())
print("Alex:",Alex.get_balance())
