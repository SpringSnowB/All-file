"""
彩票
双色球
红色：6个 1-33 不能重复
蓝色 1个 1-16
--随机产生一注彩票
--在终端中购买一注彩票
   “请输入第一个红色号码：”
   “号码超过范围”
   “号码已存在”
"""
import random
list_lottery = []
list_red = []
list_bule = [random.randint(1,16)]
j = 1
while j <=6:
    temp = random.randint(1,33)
    if temp not in list_red:
        list_red.append(temp)
        j +=1
print(list_red)
print(list_bule)
list_lottery = list_red+list_bule
print(list_lottery)
list_buy = []
i = 1
while 1<=i<=6 :
    buy = int(input("请输入第%d个红球号码："%(i)))
    if buy in list_buy:
        print("号码已存在")
    elif buy not in range(1,34):
        print("号码超出范围")
    else:
        list_buy.append(buy)
        i +=1
print(i)
while i <= 7:
    buy = int(input("请输入蓝色球号码："))
    if buy in range(1,17):
        list_buy.append(buy)
        i += 1
    else:
        print("号码超出范围")

print(list_buy)