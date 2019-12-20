"""
在终端中录入你喜欢的人，如果是空字符串，则打印
所有人（一个一行）
前三个人
总人数
"""

list_like = []
name = input("请输入你喜欢的人名字：")
while name:
    list_like.append(name)
    name = input("请输入你喜欢的人名字：")
else:
    for item in list_like:
        print(item)
    print(list_like[:3])
    print(len(list_like))
