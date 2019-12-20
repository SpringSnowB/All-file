"""
使用列表推导式 1-50之间能被3或5整除的数字
5-20之间数字的三次方
"""

list_3_5 = [item for item in range(1,51) if item % 3 == 0 or item % 5 == 0]
list_5_20 = [item ** 3 for item in range(5,21)]
print(list_3_5)
print(list_5_20)