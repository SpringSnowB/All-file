"""
将迭代器版本的员工管理器改为yield版本的
"""
class StaffManager:
    def __init__(self, name="", age=0, sex=""):
        self.name = name
        self.age = age
        self.sex = sex
        self.__list_staff = []
        self.__list_index = 0
    def add_staff(self,name="",age=22,sex=""):
        dict_staff = {}
        dict_staff["姓名"] = name
        dict_staff["年龄"] = age
        dict_staff["性别"] = sex
        self.__list_staff.append(dict_staff)

    def __iter__(self):
        while self.__list_index < len(self.__list_staff):
            yield self.__list_staff[self.__list_index]
            self.__list_index += 1
        # for item in self.__list_staff:
        #     yield item
manager = StaffManager()
manager.add_staff("kk",23,"f")
manager.add_staff("dd",28,"m")
manager.add_staff("ss",29,"f")
for item in manager:
    print(item)