"""
删除大于10 的元素
列表中删除某些东西，倒序删除绝对正确
"""
list_number = [5,6,17,78,34,5]
# for i in range(len(list_number)):
#     if list_number[i] > 10:
#         del list_number[i]   #索引越界，错误写法
# for item in list_number:
#     if item > 10:
#         list_number.remove(item) #漏删部分元素（后面元素向前移动）错误写法

for i in range(len(list_number)-1,-1,-1):  #倒序删除
    if list_number[i] > 10:
        del list_number[i]
print(list_number)
