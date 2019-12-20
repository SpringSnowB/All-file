
class Enemy:

    def __init__(self, name, boold, attack, defense):
        self.name = name
        self.boold = boold
        self.attack = attack
        self.defense = defense #alt + 回车 自动生成参数

    @property
    def boold(self):
        return self.__boold

    @boold.setter
    def boold(self,value):
        if value in range(0,1001):
            self.__boold = value
        else:
            raise Exception("OUT OF RANGE 1-1000")

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self,value):
        if value in range(0,501):
            self.__attack = value
        else:
            raise Exception("out of range 1 - 500")

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        if value in range(0, 101):
            self.__defense = value
        else:
            raise Exception("out of range 1 - 100")


    def print_info(self):
        print("%s血量%d 攻击力%d 防御力%d"%(self.name,self.boold,self.attack,self.defense))

Enemy("八奇大蛇",1000,490,100)