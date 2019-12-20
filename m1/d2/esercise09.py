"""
录入总秒数，计算几小时几分钟几秒钟

"""
second_count = int(input("请输入总秒数："))
hour = second_count//3600
minute = second_count%3600//60
second = second_count%3600%60
print(str(hour)+"小时"+str(minute)+"分钟"+str(second)+"秒")