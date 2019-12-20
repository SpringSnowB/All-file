"""
创建技能类（数据：技能名称,冷却时间,消耗法力,攻击比例）
                          0-60    0-100   0 - 1
"""
class Ability:
    def __init__(self, skill=0, cooling=0, power=0, atk_percentage=0):
        self.skill = skill
        self.cooling = cooling
        self.power = power
        self.atk_percentage = atk_percentage


    @property
    def cooling(self):
        return self.__cooling
    @cooling.setter
    def cooling(self,value):
        if 0 <= value <= 60:
            self.__cooling = value
        else:
            raise Exception("超出范围 0-100")

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if 0 <= value <= 100:
            self.__power = value
        else:
            raise Exception("超出范围 0-60")

    @property
    def atk_percentage(self):
        return self.__atk_percentage

    @atk_percentage.setter
    def atk_percentage(self, value):
        if 0 <= value <= 1:
            self.__atk_percentage = value
        else:
            raise Exception("超出范围 0-60")

    def print_info(self):
        print("技能：%s 冷却时间：%d 消耗法力：%d 攻击比例：%.2f."%(self.skill,self.cooling,self.power,self.atk_percentage))


man1 = Ability("XXX",55,80,0.12)
man1.print_info()