class Dog:
    def __init__(self, pet_name = "", breed = "", price=3000):
        self.pet_name = pet_name
        self.breed = breed
        self.price = price

    def shout(self):
        print(self.pet_name, "旺旺叫")

# 1.
d01 = Dog("米咻","拉不拉多")
d02 = d01
d01.pet_name = "小黄"
print(d02.pet_name)# ?

# 2.
def fun01(p1):
    p1.price = 2000
fun01(d01)
print(d01.price)
# 3.
list01 = [
    d01,
    d02,
    Dog("小白","萨魔")
]
list02 = list01[:]
list01[2].pet_name = "小志"
print(list02[2].pet_name)
