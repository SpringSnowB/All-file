"""
在终端中录入字符串，如果录入空，则打印所有
"""
list_result = []

while True:
    string = input("请输入：")
    if string == "":
        break
    list_result.append(string)
list_str ="".join(list_result)
print(list_str)