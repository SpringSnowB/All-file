"""
队列
"""

class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        self.__list.append(item)

    def dequeue(self):
        if not self.__list:
            return None
        return self.__list.pop(0)

    def isEmpty(self):
        if not self.__list:
            return True
        return False

    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue('op')
    print(queue.dequeue())
    queue.enqueue(True)
    print(queue.isEmpty())
    print(queue.size())