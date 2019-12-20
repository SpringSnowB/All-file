"""
录入多位真整数，计算每位相加和

"""
count = 0
number = input("请输入一个多位整数：")
for item in number:
    count += int(item)
print(count)