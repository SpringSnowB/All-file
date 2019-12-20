"""
获取数字/运算符/
如果运算符是 + - × 打印结果，否则打印运算符有误
"""
munber1 =float(input("请输入数字1："))
munber2 =float(input("请输入数字2："))
sign = input("请输入运算符：")
if sign =="+":
    print(str(munber1+munber2))
elif sign =="-":
    print(str(munber1-munber2))
elif sign =="*":
    print(str(munber1*munber2))
elif sign =="/":
    print(str(munber1/munber2))
else:
    print("运算符错误！")