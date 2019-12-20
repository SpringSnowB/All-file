"""
定义图形管理器，记录多个图形
迭代图形管理器，获取多个图形
"""
class GraphManagerIterator:
    def __init__(self,data):
        self.__data = data
        self.__index = 0
    def __next__(self):
        if self.__index ==len(self.__data):
            raise StopIteration
        item = self.__data[self.__index]
        self.__index += 1
        return item

class GraphManager:
    def __init__(self):
        self.__list_graph = []
    def add_graph(self,graph):
        self.__list_graph.append(graph)
    def __iter__(self):
        return GraphManagerIterator(self.__list_graph)

manager = GraphManager()
manager.add_graph("*")
manager.add_graph("%")
manager.add_graph("#")
for item in manager:
    print(item)