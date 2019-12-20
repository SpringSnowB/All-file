"""
创建老婆列表（姓名，身高，体重，年龄）
定义函数，在老婆列表中查找身高在160--170之间的所有老婆
定义函数，在老婆列表中查找年龄在25--30之间的所有老婆姓名与年龄
"""
class WifeModel:
    def __init__(self, name="", height=160, weight=55, age=25):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
    def __str__(self):
        return "%s,%d,%d,%d"%(self.__name,self.__height,self.__weight,self.__age)

class WifeManager:
    def __init__(self):
        self.__list_wife =[]

    def add_wife(self,name="", height=160, weight=55, age=25):
        dict_wife = {}
        dict_wife["姓名"]=name
        dict_wife["身高"]=height
        dict_wife["体重"]=weight
        dict_wife["年龄"]=age
        self.__list_wife.append(dict_wife)

    def search_height(self,value1,value2):
        for item in self.__list_wife:
            if value1 <= item["身高"] <= value2:
                yield item

    def search_age(self,age1,age2):
        for item in self.__list_wife:
            if age1 <= item["年龄"] <= age2:
                yield item

    def search_name(self,name):
        for item in self.__list_wife:
            if item["姓名"]==name:
                yield item

    def search_weight(self, value1, value2):
        for item in self.__list_wife:
            if value1 <= item["体重"] <= value2:
                yield item

wife_manager = WifeManager()
wife_manager.add_wife("kk",165,46,21)
wife_manager.add_wife("kk",167,46,21)
wife_manager.add_wife("kk",163,46,21)
wife_manager.add_wife("kk",161,46,21)
wife_manager.add_wife("ku",155,53,26)
wife_manager.add_wife("rr",168,56,28)
wife_manager.add_wife("kjk",175,66,48)
for item in wife_manager.search_age(25,30):
    print(item)
for item in wife_manager.search_height(165,170):
    print(item)

result = tuple(wife_manager.search_name("kk"))
print(result[-1])