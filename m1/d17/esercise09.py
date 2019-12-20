"""
定义函数，在老婆列表中查找所有年龄大于25的所有老婆对象
定义函数，在老婆列表中查找身高小于180的所有老婆对象
"""
class Wife:
    def __init__(self, name="",height=160,weight=50,age=22):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def __str__(self):
        return "%s,%d,%d,%d"%(self.name, self.height, self.weight, self.age)

list_wife = [
    Wife("KK",156,53,38),
    Wife("KK",156,53,38),
    Wife("KK",156,53,38),
    Wife("KK",156,53,38),
    Wife("DD",166,40,22),
    Wife("SS",178,51,27),
    Wife("aa",164,68,25),
]
def find(list_wife,func):
    for item in list_wife:
        if func(item):
            yield item

def find_age(item):
    return item.age > 25

def find_height(item):
    return item.height < 180

for item in find(list_wife,find_age):
    print(item)

result01 = tuple(find(list_wife,find_age))
result02 = tuple(find(list_wife,find_height))
print(result01)
print(result02)