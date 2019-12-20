"""
定义员工管理器
    1.存储所有员工
    2.提供计算总薪资的方法
    普通员工：底薪
    程序员：底薪+项目分红
    测试员：底薪 + BUG数×5
    需求变化
        销售......
    要求：指出代码体现的三大特征与六个原则
"""

class StaffManager:
    def __init__(self):
        self.__list_staff = []

    def store_staff(self,staff):
        self.__list_staff.append(staff)

    def calculate_staff_slary(self):
        sum_slary = 0
        for item in self.__list_staff:
            sum_slary += item.calculate_slary()
        return sum_slary

class Staff:
    def __init__(self, base_slary=3000):
        self.base_slary = base_slary
    def calculate_slary(self):
        return self.base_slary

class OrdinaryStaff(Staff):
    def __init__(self, base_slary=3000):
        super().__init__(base_slary)

    def calculate_slary(self):
        return super().calculate_slary()


class Programmer(Staff):
    def __init__(self, base_slary=6000, bonus=0):
        super().__init__(base_slary)
        self.bonus = bonus

    def calculate_slary(self):
        return super().calculate_slary()+self.bonus  #在爹的基础上加上新的东西--->扩展重写（里氏原则）

class TestEngineer(Staff):

    def __init__(self, base_slary=5000, bug_number=0):
        super().__init__(base_slary)
        self.bug_number = bug_number

    def calculate_slary(self):
        return super().calculate_slary()+self.bug_number*5


manager = StaffManager()
manager.store_staff(TestEngineer(5500,5))
manager.store_staff(Programmer(8000,3000))
sum_slary = manager.calculate_staff_slary()
print(sum_slary)