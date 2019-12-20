"""
    "水仙花数":各位数字立方和等于该数本身
    定义函数，根据位数计算水仙花数
    输入：3
    输出：[153, 370, 371, 407]
"""


def is_daffodil(number):
    """
        判断指定数字是否为水仙花数
    :param number: int 类型，表示需要判断的数字
    :return: bool 类型，表示是否为水仙花数。
    """
    str_number = str(number)
    power = len(str_number)
    sum_value = 0
    for item in str_number:
        sum_value += int(item) ** power
    return sum_value == number


def get_daffodil(n):
    """
        获取指定位数的水仙花数
    :param n:int类型，表示整数位数。
    :return:列表类型，水仙花数。
    """
    # list_list = []
    # for i in range(10 ** (n - 1), 10 ** n):
    #     if is_daffodil(i):
    #         list_list.append(i)
    # return list_list
    return [num for num in range(10 ** (n - 1), 10 ** n) if is_daffodil(num)]


print(get_daffodil(4))
