"""
定义图形管理器
1、存储所有图形
2、计算所有图形的面积
需求变化：
还可能增加新图形
要求：图形管理器满足开闭原则
"""
class Graphics:
    def __init__(self, name=""):
        self.name = name

    def calculate_area(self):
        pass

class Tangle(Graphics):

    def __init__(self, name="三角形", bottom_side=0, height=0):
        super().__init__(name)
        self.bottom_side = bottom_side
        self.height = height

    def calculate_area(self):
        super().calculate_area()
        return self.bottom_side*self.height/2

class Rectangle(Graphics):

    def __init__(self, name="矩形", height=0, wide=0):
        super().__init__(name)
        self.height = height
        self.wide = wide

    def calculate_area(self):
        super().calculate_area()
        return self.height*self.wide


class GraphicsManager:
    def __init__(self):
        self.__list_graphics = []

    def store_graphics(self,graphics):
        self.__list_graphics.append(graphics)

    def calculate_area(self):
        sum_area = 0
        for item in self.__list_graphics:
            sum_area += item.calculate_area()
        return sum_area

manager = GraphicsManager()
manager.store_graphics(Tangle(bottom_side=4,height=10))
manager.store_graphics(Rectangle(height=9,wide=7))
sum = manager.calculate_area()
print(sum)