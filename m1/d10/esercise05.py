"""
对象计数器
利用类变量统计
"""
class Wife:
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Wife.count += 1
    def play(self):
        print(self.name,"play")



w1 = Wife("XXX",48)
W2 = Wife("AA",24)
print(Wife.count)