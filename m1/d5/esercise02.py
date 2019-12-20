"""
在列表找出最大值，不用max()
"""
list_max = [23,4,5,68,43,67,866,78,453,32,134,1024]
max_number = list_max[0]
for i in range(1,len(list_max)):  #从第一个开始比较
    if max_number < list_max[i]:
        max_number = list_max[i]
    else:
        continue
print(max_number)