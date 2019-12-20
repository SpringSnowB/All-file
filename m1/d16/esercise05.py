"""
生成器
"""


class MyRangeIterator:
    def __init__(self, end):
        self.__end = end
        self.__number = 0
    def __next__(self):
        if self.__number == self.__end:
            raise StopIteration
        item = self.__number
        self.__number += 1
        return item

class MyRange:
    def __init__(self,data):
        self.__data = data

    def __iter__(self):
        return MyRangeIterator(self.__data)

for item in MyRange(15):
    print(item)