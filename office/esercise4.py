"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

def find(target,array):
    if len(array)==0 or len(array[0])==0:
        return False
    if target<array[0][0] or target >array[len(array)-1][len(array[0])-1]:
        return False
    row = len(array)-1
    col = 0
    while row >= 0 and col < len(array[0]):
        if target > array[row][col]:
            col += 1
        elif target < array[row][col]:
            row -= 1
        else:
            return True
    return False

a =[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(find(1,[[]]))