"""
猜拳
"""
# import random
# gass = input("请输入：")
# tuple_gass = ('石头','剪刀','布')
# string_gass = tuple_gass[random.randint(0,2)]
# if gass == "石头" and string_gass == "剪刀":
#     print("WIN!")
# elif gass == "剪刀" and string_gass == "布":
#     print("WIN!")
# elif gass == "布" and string_gass == "石头":
#     print("WIN!")
# elif gass == string_gass :
#     print("平局!")
# else:
#     print("LOSE!")
# print(string_gass)


import random
input_gass = input("你出：")
tuple_gass = ('石头','剪刀','布')
system_gass = tuple_gass[random.randint(0,2)]
tuple_win = (
    ("石头","剪刀"),
    ("剪刀","布"),
    ("布","石头")
)

tuple_input_system = (input_gass,system_gass)
if tuple_input_system in tuple_win:
    print("WIN!")
elif input_gass == system_gass:
    print("平局")
else:
    print("LOSE！")
print("系统出："+system_gass)
#容器的思想，统一管理数据