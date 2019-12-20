"""
在终端中录入小时数，分钟数，秒数，计算总秒数
"""

hour =int(input("请输入小时："))
minute = int(input("请输入分钟："))
second = int(input("请输入秒："))
result = hour*3600+minute*60+second
print(str(result))
