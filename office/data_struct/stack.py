"""
栈的操作
"""

# 创建栈
class Stack:
    def __init__(self):
        self.__list = []

    #判断栈是否为空
    def is_empty(self):
        if not self.__list:
            return True
        return False

    #添加一个新元素到盏顶
    def push(self,item):
        self.__list.append(item)

    #返回栈顶元素
    def peek(self):
        if not self.__list:
            return None
        return self.__list[len(self.__list)-1]

    #返回栈顶元素，并删除栈顶元素
    def pop(self):
        if not self.__list:
            return None
        return self.__list.pop()

    #返回栈中元素个数
    def size(self):
        return len(self.__list)

if __name__=='__main__':
    stack = Stack()
    stack.push('aaa')
    print(stack.size())
    stack.push(8)
    stack.push(True)
    print(stack.peek())
    print(stack.size())
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())



