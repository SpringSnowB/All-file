"""
定义函数，根据时/分/秒计算总秒数
"""
def figure_second(hour = 0,minute = 0,second = 0):
    return hour*3600+minute*60+second



print(figure_second(hour= 1,second=9))
print(figure_second(1,9,9))
print(figure_second(hour=2))