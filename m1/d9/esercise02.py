"""
    定义函数，判断二维数字列表中是否存在某个数字
    输入：二维列表、11
    输出：True/False
"""
map = [
    [2, 0, 2, 0],
    [2, 4, 0, 2],
    [0, 0, 2, 0],
    [2, 4, 4, 2],
]


def find_number_in_list(list_find,number_find):
    for line in list_find:
        for number_find in line:
            return True
    return False

print(find_number_in_list(map,4))