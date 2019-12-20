"""
比较四个数大小
"""
wight1 = float(input("请输入第一个人的体重："))
wight2 = float(input("请输入第二个人的体重："))
wight3 = float(input("请输入第三个人的体重："))
wight4 = float(input("请输入第四个人的体重："))
# if wight1>=wight2 and wight1>=wight3 and wight1>=wight4:
#     print("最重的是："+str(wight1))
# elif wight2>=wight3 and wight2>=wight4:
#     print("最重的是："+str(wight2))
# elif wight3>=wight4:
#     print("最重的是：" + str(wight3))
# else:
#     print("最重的是：" + str(wight4))


i = wight1
if i < wight2:
    i = wight2
if i < wight3:
    i = wight3
if i < wight4:
    i = wight4
print("最重的是："+str(i))