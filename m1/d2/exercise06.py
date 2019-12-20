"""
//取整数
收银台
在终端中录入商品单价　购买数量　支付金额
计算应找回多少钱
"""
# charge = float(input("please input the price of good:"))
# number = int(input("please input how many you bought:"))
# payment = float(input("please input how much you paid:"))
# print("return:"+str(payment-charge*number))

# weight_liang = int(input("请输入两:"))
# weight_jin = weight_liang//16
# weight_liang_liang=weight_liang%16
# print("是"+str(weight_jin)+"斤"+str(weight_liang_liang)+"两")

# 距离＝加速度＊时间平方的一半＋初速度＊时间
# 已知距离　时间　初速度　求加速度
# length = float(input("请输入距离："))
# time = float(input("请输入时间（s）："))
# v0 = float(input("请输入初速度："))
# print("加速度为："+str((length-v0*time)/(time**2)*2))

#录入四位整数，计算每位相加
number = int(input("请输入一个四位数："))
result = number//1000
result += number//100%10
result += number//10%10
result += number%10
print(result)