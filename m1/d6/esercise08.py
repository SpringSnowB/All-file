"""
在终端中录入人名，要求不能重复
如果空则停止，打印所有人名
集合是无序的
"""
set_name = set()
while True:
    name = input("请输入人名：")
    if name == "":
        break
    set_name.add(name)
for item in set_name:
    print(item)