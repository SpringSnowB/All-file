"""
创建手雷类，定义爆炸方法
当爆炸时，有可能会伤害敌人，也可能会伤害玩家
需求变化：
房子、树、鸭子
"""
class Frag:
    def explode(self,matter):
        print("手雷炸了")
        matter.injured()

class Injured:
    def injured(self):
        pass

class PlayInjured(Injured):
    def injured(self):
        print("玩家受伤")

class EmeryInjured(Injured):
    def injured(self):
        print("敌人受伤")
class HouseInjured(Injured):
    def injured(self):
        print("房子倒了")


play = PlayInjured()
house = HouseInjured()
bomb = Frag()
bomb.explode(play)
bomb.explode(house)