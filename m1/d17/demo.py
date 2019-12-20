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


def find01(list_target):
    for item in list_target:
        if 160 <= item.height <= 170:
            yield item


def find02(list_target):
    for item in list_target:
        if 25 <= item.age <= 30:
            yield (item.name, item.age)


# ------------------------------
# 测试

list01 = [
    Wife("铁锤", 27, 190, 200),
    Wife("铁钉", 37, 165, 160),
    Wife("铁棒", 24, 160, 190),
    Wife("铁锅", 23, 190, 100),
]

for item in find01(list01):
    print(item)

for item in (item for item in list01 if 160 <= item.height <= 170):
    print(item)

for item in ((item.name, item.age) for item in list01 if 25 <= item.age <= 30):
    print(item)

# 惰性操作/延迟操作
# 优点：节省内存
# 缺点：不同灵活(索引、切片)访问

# 立即操作
# 优点：灵活(索引、切片)访问
# 缺点：占用内存过多

# 惰性操作 --> 立即操作
result = tuple(find01(list01))
print(result[-1])


# -- 定义函数，在老婆列表中查找"铁钉"老婆对象
def find03(list_target):
    for item in list_target:
        if item.name == "铁钉":
            return item

result = find03(list01)
print(result)

# -- 定义函数，在老婆列表中查找体重在40- - 60之间的所有老婆
def find04(list_target):
    for item in list_target:
        if 40 <= item.weight <= 60:
            yield item

# 惰性操作
for item in find04(list01):
    print(item)

# 立即操作
result = list(find04(list01))
print(result[0])