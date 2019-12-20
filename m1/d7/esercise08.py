"""
将一维列表多行打印

调试F8逐过程调试，会跳过函数
调试F7逐语句调试
"""
def print_list(list_print):
    """
    多行打印一维列表
    :param list_print: 所要打印的列表
    :return:
    """
    for item in list_print:
        print(item)

print_list([13,23,421,43,643,23,42,90])