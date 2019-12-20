"""
创建类
车（品牌、价格）
创建子类
电动车（电池容量、充电速度）
画出内存图
"""
class Car:
    def __init__(self, brand="", price=0):
        self.brand = brand
        self.price = price

class Electrombile(Car):
    def __init__(self, brand="", price=0, battery_capacity=0, charging_rate=0):
        super().__init__(brand,price)
        self.battery_capacity = battery_capacity
        self.charging_rate = charging_rate

electrombile = Electrombile("爱玛",3900,10000,500)
