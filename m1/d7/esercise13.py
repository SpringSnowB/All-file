"""
定义函数，将二维列表以表格状打印在终端中
"""
def print_double_list(double_list):
    for r in range(len(double_list)):
        for c in double_list[r]:
            print(c,end="\t")
        print()

print_double_list([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])