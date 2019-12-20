"""
程序产生一个1-100的随机数，猜数字，直到猜对
"""
import random
number = random.randint(1,100)
count = 0
while count < 5:
    grass = int(input("请输入数字："))
    count += 1
    if grass == number:
        print("猜对了，一共猜了"+str(count)+"次")
        break
    elif grass >number:
        print("猜错啦，请往小一点猜")
    else:
        print("猜错啦，请往大一点猜")
else:
    print("游戏结束，没猜对，好笨哦！")