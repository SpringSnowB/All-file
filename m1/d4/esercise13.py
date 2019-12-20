"""
判断一个字符串是否是回文
上海自来水来自海上
"""

list_string = list(input("请输入一串字符："))
list_back = []
# print(list_string)
for item in list_string:
    list_back.insert(0,item)
# print(list_back)
if list_string == list_back:
    print("是回文！")
else:
    print("不是回文！")

# if list_string == list_string[::-1]:
#     print("是回文！")
# else:
#     print("不是回文！")


