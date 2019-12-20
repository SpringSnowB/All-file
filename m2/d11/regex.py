import re

#目标字符串

s = "Aplex:1998,Sunny:1997"

# #正则表达式
pattern = r"\w+:\d+"

#使用findall是不能加子组的，加子组后之匹配子组内容
l = re.findall(pattern,s)
print(l)

regex = re.compile(pattern)
l = regex.findall(s,1,17)
print(l)#['plex:1998']

#分割字符串
l = re.split(r'[:,]',s,2)
print(l)#['Aplex', '1998', 'Sunny:1997']


#替换
l = re.sub(r':','——',s,1)#Aplex——1998,Sunny:1997
print(l)#Aplex——1998,Sunny——1997

l = re.subn(r':','——',s)
print(l)#('Aplex——1998,Sunny——1997', 2)



