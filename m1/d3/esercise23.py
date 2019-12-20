month = int(input("请输入月份（数字）："))
if month < 1 or month >12:
    print("ERROR!")
elif month in [1, 2, 3]:
    print("第一季度")
elif month in [ 4, 5, 6]:
    print("第二季度")
elif month in [ 7, 8, 9]:
    print("第三季度")
else:
    print("第四季度")