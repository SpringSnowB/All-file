"""
元组是按需分配，列表预留空间，元素固定不更改是按需分配，用元祖
"""
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("ERROR")
elif month == 2:
    print("28")
elif month in (4,6,9,11):
    print("30")
else:
    print("31")