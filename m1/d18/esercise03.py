"""
定义函数，在，老婆列表中，删除年龄在20-25之间的所有老婆
定义函数，在，老婆列表中，删除体重大于160的所有老婆
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


list01 = [
    Wife("铁锤", 27, 190, 200),
    Wife("铁钉", 37, 165, 160),
    Wife("铁棒", 24, 160, 190),
    Wife("铁锅", 23, 190, 100),
]

from d18.common.IterableHelper import IterableHelper
# print(IterableHelper.remove_wife(list01,lambda item:20<item.age<25))
# print(IterableHelper.remove_wife(list01,lambda item:item.weight>160))

"""
在老婆列表中找出年龄最大的老婆
在老婆列表中找出身高最高的老婆
"""
# print(IterableHelper.find_max(list01,lambda max_wife,item:max_wife.age<item.age))
# print(IterableHelper.find_max(list01,lambda max_wife,item:max_wife.weight<item.weight))

"""
定义函数，根据体重对老婆进行升序排列
定义函数，根据身高对老婆进行升序排列
"""
for item in IterableHelper.sort_wife(list01,lambda item:item.weight):
    print(item)
print("-----------------------")
for item in IterableHelper.sort_wife(list01,lambda item:item.height):
    print(item)