"""
创建杯子类
"""
class Cup:
    def __init__(self,type,capacity,color):
        self.type = type
        self.capacity = capacity
        self.color = color

    def take_in_water(self):
        print("%s的%s杯子可以盛%dml水"%(self.color,self.type,self.capacity))


cup1 = Cup("富士光",500,"白色")
cup2 = Cup("Bottle",800,"粉色")
cup3 = Cup("富士光",500,"红色")

cup1.take_in_water()
cup2.take_in_water()
cup3.take_in_water()