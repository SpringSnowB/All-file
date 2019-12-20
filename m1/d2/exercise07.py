"""
录入一个年份，判断是否是润年
条件　能被４整除不被１００整除或者能被４００整除
"""
year = int(input("请输入年份："))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print(True)
# else:
#     print(False)
result = year%4==0 and year%100!=0 or year%400==0#布尔直接赋值
print(result)