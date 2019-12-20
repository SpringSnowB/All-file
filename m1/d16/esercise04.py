"""
定义员工管理器，记录多个员工
迭代员工管理器，获取多个员工
"""
class StaffManagerIterator:
    def __init__(self, data):
        self.__list_index = 0
        self.__data = data
    def __next__(self):
        if self.__list_index == len(self.__data):
            raise StopIteration()
        item = self.__data[self.__list_index]
        self.__list_index += 1
        return item


class StaffManager:
    def __init__(self, name="", age=0, sex=""):
        self.name = name
        self.age = age
        self.sex = sex
        self.__list_staff = []
    def add_staff(self,name="",age=22,sex=""):
        dict_staff = {}
        dict_staff["姓名"] = name
        dict_staff["年龄"] = age
        dict_staff["性别"] = sex
        self.__list_staff.append(dict_staff)

    def __iter__(self):
        return StaffManagerIterator(self.__list_staff)

manager = StaffManager()
manager.add_staff("kk",23,"f")
manager.add_staff("dd",28,"m")
manager.add_staff("ss",29,"f")
for item in manager:
    print(item)