"""
 根据面向对象思想，描述下列情景。
    玩家攻击敌人，敌人受伤(减血,加分)后可能死亡(掉落装备)。
    敌人攻击玩家，玩家受伤(减血,碎屏)后可能死亡(游戏结束)。
    [行为的不同要用类区分]
"""
class Enemy:
    def __init__(self, name="", atk=0, hp=0, equipment=""):
        self.name =name
        self.atk =atk
        self.hp =hp
        self.equipment = equipment

    def attack(self,player):
        player.broken_screen()
        player.injured(self.atk)


    def injured(self,atk):
        self.hp -= atk
        if self.hp <= 0:
            self.dead()


    def dead(self):
        print(self.name+"死亡，掉落"+self.equipment)


class Player:
    def __init__(self, name="", atk=0, hp=0, score=0):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.score = score

    def attack(self,enemy):
        enemy.injured(self.atk)
        self.awarded_mark()

    def injured(self, atk):
        self.hp -= atk
        if self.hp <= 0:
            self.dead()

    def broken_screen(self):
        print("碎屏")

    def awarded_mark(self):
        print("加10分")
        self.score += 10

    def dead(self):
        print("game over!")

play01 =Player("WB",50,100)
enemy01 = Enemy("GZ",100,120,"money")
play01.attack(enemy01)
enemy01.attack(play01)