"""
使用面向对象思想描述下列情景：
小明在银行取钱
"""

class Person:
    def __init__(self, name="", money=0):
        self.name=name
        self.money = money

class Bank:
    def __init__(self,money=0):
        self.money = money

    def draw_money(self,person,value):
        #银行钱减少，人的钱增加
        self.money -=value
        person.money += value

xm = Person("XM")
b01 = Bank(10000)
b01.draw_money(xm,1000)
print("人的钱：",xm.money)
print("bank的钱：",b01.money)