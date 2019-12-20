"""

id() 查看内存地址
ord() 查看编码值   字--->数
chr() 将编码值转换成字   数————>字
"""
# string = input("请输入：")
# for item in string:
#     print(ord(item))

number = input("请输入：")
while number:
    print(chr(int(number)))
    number = input("请输入：")
