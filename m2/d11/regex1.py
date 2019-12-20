import re

s = "今年是2019年12月10日，2019年初的目标实现了吗？"
pattern = r'\d+'

#获取匹配内容的迭代器
result = re.finditer(pattern,s)
for i in result:
    #迭代得到没出匹配内容的match对象
    print(i.group())#通过group()可以获取到match对象对应的内容

#完全匹配
obj = re.fullmatch(r'.+',s)
print(obj)

#匹配开始位置
obj = re.match('\w+',s)
print(obj)

#匹配第一处数字
obj = re.search('\d+',s)
print(obj.group())