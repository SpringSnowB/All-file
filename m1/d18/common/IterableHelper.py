class IterableHelper:
    @staticmethod
    def find(iterable,func):
        """
        通用的筛选元素
        :param iterable:需要被筛选的可迭代对象
        :param func: 筛选处理逻辑
        :return: 生成器类型
        """
        for item in iterable:
            yield func(item)

    @staticmethod
    def remove_wife(iterable,func):
        for item in iterable:
            if func(item):
                iterable.remove(item)
        return iterable

    @staticmethod
    def find_max(iterable,func):
        max_wife = iterable[0]
        for i in range(1,len(iterable)):
            if func(max_wife,iterable[i]):
                max_wife = iterable[i]
        return max_wife


    @staticmethod
    def sort_wife(iterable,func):
        for i in range(len(iterable)-1):
            for j in range(i+1,len(iterable)):
                if func(iterable[i]) > func(iterable[j]):
                    iterable[i],iterable[j]=iterable[j],iterable[i]
        return iterable
