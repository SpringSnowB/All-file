"""
if 条件:
    代码
else:
    代码


if 条件：
    代码
elif 条件：
    代码
else:
    代码

"""

"""
//取整数
收银台
在终端中录入商品单价　购买数量　支付金额
计算应找回多少钱
"""
charge = float(input("please input the price of good:"))
number = int(input("please input how many you bought:"))
payment = float(input("please input how much you paid:"))
result = payment-charge*number
if result>=0:
    print("return:" + str(result))
else:
    print("钱不够！")

