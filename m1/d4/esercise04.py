"""
累加10 - 50 之间各位不是2 5 9 的数字
"""
count = 0
for item in range(10,51):
    if item % 10 != 2 and item %10 !=5 and item %10 != 9:
        count += item
print(count)

# count = 0
# for item in range(10,51):
#     if item % 10 == 2 or item %10 ==5 or item %10 == 9:
#         continue
#     count += item
# print(count)