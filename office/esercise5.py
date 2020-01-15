"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
from timeit import Timer
# def replace(a):
#     return a.replace(' ','%20')
#
# print(replace('We Are Happy'))
# print(replace("hello world"))

def replace(a):
    s = ''
    for i in a:
        if i == ' ':
            s+='%20'
        else:
            s+=i
    return s

print(replace('We Are Happy'))

def replace_list(a):
    str_list = []
    for i in a:
        if i ==' ':
            str_list.append('%20')
        else:
            str_list.append(i)
    return ''.join(str_list)
print(replace_list('We Are Happy'))

# 计算时间，用字符串更快
t1 = Timer("replace('We Are Happy')",'from __main__ import replace')
t2 = Timer("replace_list('We Are Happy')",'from __main__ import replace_list')
print('replace',t1.timeit(number=100000))
print('replace_list',t2.timeit(number=100000))