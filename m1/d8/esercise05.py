"""
定义函数，多个值累加
 星号元组形参只能有一个，默认名为args，尽管写什么都行
"""

def count_number(*args):
    """
    定义函数，多个值累加
    :param args: 需要进行累加的数据
    :return:
    """
    count = 0
    for item in args:
        count += item
    return count

print(count_number(78,123,43,25))