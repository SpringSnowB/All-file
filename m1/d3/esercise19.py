"""
循环语句
while 条件：
    循环体
"""
while True:
    quarter = input("请输入季度：")
    if quarter == "春":
        print("1月2月3月")
    elif quarter == "夏":
        print("4月5月6月")
    elif quarter == "秋":
        print("7月8月9月")
    elif quarter == "冬":
        print("10月11月12月")
    else:
        print("ERRPR!")
    if input("输入e退出？") == "e":
        break
