import re
pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search("abcdefgh123")

#属性变量
print(obj.pos)#初始下标
print(obj.endpos)#结束下标+1
print(obj.lastgroup)#最后一组的名称
print(obj.lastindex)#最后一组的位置（从1开始）

print('-------------')

#属性方法
print(obj.span())#匹配内容的起止位置
print(obj.start())#获取内容开始位置
print(obj.end())#获取内容结束位置
print(obj.groupdict())#获取内容组，没有组名会被忽略
print(obj.groups())#获取所有组
print(obj.group(1))#获取指定位置的组
print(obj.group())#获取匹配的字符串
print(obj.group('pig'))#获取指定组名的组
