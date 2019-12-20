import re
s= """Hello 
 北京
"""


#只匹配ASCII
regex = re.compile(r'\w+',flags=re.A)
l = regex.findall(s)
print(l)

#不区分字母大小写
regex = re.compile(r'[a-z]+',flags=re.I)
l = regex.findall(s)
print(l)

#任意匹配
regex = re.compile(r'.+',flags=re.S)
l = regex.findall(s)
print(l)

#^ $可以匹配每行开头河结尾位置
regex = re.compile(r'^北京',flags=re.M)
l = regex.findall(s)
print(l)

