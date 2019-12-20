"""
根据面向对象思想，描述下列情景。
   张无忌 教 赵敏九阳神功
   赵敏 教 张无忌玉女心经
   张无忌上班挣了10000元
   赵敏上班挣了8000元
   [数据的不同使用对象区分]
"""
class Person:
    def __init__(self, name="", kongfu="", money=0):
        self.name = name
        self.kongfu = kongfu
        self.money = money

    def teach(self,person):
        print(self.name+"教"+person.name+self.kongfu)

    def earn_money(self,person,value):
        person.money += value


zwj = Person("zwj","九阳神功",500)
zm = Person("zm","玉女心经",800)
zwj.teach(zm)
zm.teach(zwj)
zm.earn_money(zwj,10000)
zwj.earn_money(zm,8000)
print(zwj.money)
print(zm.money)