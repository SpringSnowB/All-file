"""
    "水仙花数":各位数字立方和等于该数本身
    定义函数，根据位数计算水仙花数
    输入：3
    输出：[153, 370, 371, 407]
"""

def faffodil_number(digit):
    list_number = []
    for number in range(10**(digit-1),10**digit):
        str_number = str(number)
        sum = 0
        for i in str_number:
            sum += int(i)**len(str_number)
        if sum == number:
            list_number.append(number)
    return list_number

print(faffodil_number(4))
