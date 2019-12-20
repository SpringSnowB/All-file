"""
输入一个字符串，打印各个字符的个数
"""
string = input("请输入字符串：")
dict_string = {}
for item in string:
    if item not in dict_string:
        dict_string[item] = 1
    else:
        dict_string[item] +=1
for k ,v in dict_string.items():
    print("%s:%d"%(k,v))