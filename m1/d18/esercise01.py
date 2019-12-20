"""
1.定义函数，在老婆列表中查找所有老婆的姓名
2.定义函数，在老婆列表中查找所有老婆的姓名和身高
步骤：
1、将需求完整地实现到函数中
2、将变化点单独定义到函数中
3、将通用代码定义到函数中
4、用参数隔离变化
5、将通用代码移动到IterableHelper类中
6、测试调用IterableHelper的静态方法执行功能
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



def find_name(item):
    return item.name

# def find_name_and_height(list_wife):
#     for item in list_wife:
#         yield (item.name,item.height)
#
def find_name_and_height(item):
    return (item.name, item.height)


# def find(list_wife,func):
#     for item in list_wife:
#         yield func(item)

list01 = [
    Wife("铁锤", 27, 190, 200),
    Wife("铁钉", 37, 165, 160),
    Wife("铁棒", 24, 160, 190),
    Wife("铁锅", 23, 190, 100),
]
from d18.common.IterableHelper import IterableHelper

for item in IterableHelper.find(list01,find_name):
    print(item)

for item in IterableHelper.find(list01,find_name_and_height):
    print(item)