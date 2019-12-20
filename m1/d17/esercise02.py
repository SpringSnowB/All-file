

class GraphManager:
    def __init__(self):
        self.__list_graph = []
    def add_graph(self,graph):
        self.__list_graph.append(graph)
    def __iter__(self):
        for item in self.__list_graph:
            yield item
manager = GraphManager()
manager.add_graph("*")
manager.add_graph("%")
manager.add_graph("#")
for item in manager:
    print(item)