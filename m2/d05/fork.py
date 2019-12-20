import os

print("-----------------")
a = 1
pid = os.fork()#子进程从此处开始执行
if pid < 0:
    print("fail")

elif pid ==0:
    print("child  a=",a)#1
    a = 10000
else:
    print("parent a=",a)  #1

print("over  a=",a) #子进程10000,父进程1
