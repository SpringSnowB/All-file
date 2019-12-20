"""
在终端中录入一个数字，作为边长，打印矩形
"""
length = int(input("请输入边长："))
for item in range(length):
    if item != length-1 and item != 0 :
        print("*"+" "*(length-2)+"*")
    else:
        print("*" * length)
