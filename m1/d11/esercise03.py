"""
使用面向对象思想描述下列情景：
   防守者攻击敌人，敌人受伤，还能死掉
"""

class Enemy:
    def __init__(self, name, boold, attack, defense):
        self.name = name
        self.boold = boold
        self.attack = attack
        self.defense = defense #alt + 回车 自动生成参数

    def damage(self,atk):
        print(self.name+"被攻击")
        self.boold -= atk
        if self.boold <= 0:
            self.dead()

    def dead(self):
        print(self.name,"死掉")


class Defenser:
    def __init__(self, name, boold, attack, defense):
        self.name = name
        self.boold = boold
        self.attack = attack
        self.defense = defense

    def attack_enemy(self,enemy):
        enemy.damage(self.attack)


d1 = Defenser("XXX",899,500,50)
e1 = Enemy("xw",1000,500,300)
d1.attack_enemy(e1)
d1.attack_enemy(e1)