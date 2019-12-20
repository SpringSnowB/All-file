"""
创建敌人类
    -- 数据:名称,血量,攻击力,防御力
    -- 行为:打印个人信息
    -- 创建敌人列表
    -- 在敌人列表中查找"灭霸"对象
    -- 在敌人列表中查找所有死人
    -- 在敌人列表中查找攻击力最大的敌人
    -- 根据防御力,对敌人列表进行降序排列.
"""
class Enemy:

    def __init__(self, name, boold, attack, defense):
        self.name = name
        self.boold = boold
        self.attack = attack
        self.defense = defense #alt + 回车 自动生成参数


    def print_info(self):
        print("%s血量%d 攻击力%d 防御力%d"%(self.name,self.boold,self.attack,self.defense))

list_enemy = [
    Enemy("灭霸",1000,500,600),
    Enemy("刑天",0,480,300),
    Enemy("八奇大蛇",10000,1590,1600),
    Enemy("青行灯",1000,680,750),
    Enemy("黑晴明",0,800,700)
]


def find_mieba():
    for item in list_enemy:
        if item.name =="灭霸":
            item.print_info()


def find_dead():
    for item in list_enemy:
        if item.boold == 0:
            item.print_info()

def find_max_attack():
    max_attack = list_enemy[0]
    for item in list_enemy:
        if item.attack > max_attack.attack:
            max_attack = item
    max_attack.print_info()

def sort_by_defense():
    for i in range(len(list_enemy)-1):
        for j in range(i+1,len(list_enemy)):
            if list_enemy[i].defense < list_enemy[j].defense:
                list_enemy[i],list_enemy[j]=list_enemy[j],list_enemy[i]

find_dead()
print("--------------------------------")
find_mieba()
print("--------------------------------")
find_max_attack()
print("--------------------------------")
sort_by_defense()
for item in list_enemy:
    item.print_info()
print("--------------------------------")

