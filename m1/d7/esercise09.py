"""
return 后面没有数据或没有return 会返回None
录入多位整数，计算每位相加和

"""

def int_count(number):
    """
    整数累加
    :param number:输入的一串数字
    :return:
    """
    count = 0
    for item in number:
        count +=int(item)
    return count


number_string = input("请输入一个多位整数：")
print(int_count(number_string))