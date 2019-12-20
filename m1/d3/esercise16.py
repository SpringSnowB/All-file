"""
输入月份，打印天数
"""
month = int(input("请输入月份（数字）："))
if month < 1 or month > 12:
    print("ERROR!")
elif month == 2:
    print("28天")
elif month in [4, 6, 9, 11]:
    print("30天")
else:
    print("31天")