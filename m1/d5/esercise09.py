"""
根据月日，计算是一年的第几天
"""
days_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)

month = int(input("请输入月:"))
day = int(input("请输入日："))
# count = day
# for i in range(len(days_of_month)):
#     if i < month-1:
#         count +=days_of_month[i]
# print(count)


#传统思想
# count = day
# for i in range(month-1):
#     count +=days_of_month[i]
# print(count)

count = day
count +=sum(days_of_month[:month-1])
print(count)