"""
1.定义函数，在老婆列表中累加所有老婆的总身高
2.定义函数，在老婆列表中累加所有老婆的总体重
"""
class Wife:
    """
        抽象的数据
    """

    def __init__(self, name="", age=0, height=0, weight=0):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.age, self.height, self.weight)


def count_height(item):
    return item.height
def count_weight(item):
    return item.weight

def count(iterable,func):
    count= 0
    for item in iterable:
        count += func(item)
    return count
list01 = [
    Wife("铁锤", 27, 190, 200),
    Wife("铁钉", 37, 165, 160),
    Wife("铁棒", 24, 160, 190),
    Wife("铁锅", 23, 190, 100),
]
print(count(list01,count_weight))
print( count(list01,lambda item:item.height))