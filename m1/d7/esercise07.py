"""
函数 def
"""
def print_rectangle():
    """
    打印矩形
    :return:
    """
    for i in range(6):
        for j in range(4):
            if i % 2 != 0:
                print("#", end="")
            else:
                print("*", end="")
        print("")

def print_rectangle_row_column(row,column):
    """

    :param count:
    :return:
    """
    for i in range(row):
        for j in range(column):
            if i % 2 != 0:
                print("#", end="")
            else:
                print("*", end="")
        print("")

print_rectangle()

print_rectangle_row_column(9,3)