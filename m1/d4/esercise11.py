"""
1.创建列表，存储 水星、金星、地球、木星、天王星、海王星

"""
list1 = ['水星','金星','地球','木星','天王星']
print(list1)
list1.append('海王星')
list1.insert(3,'火星')
print(list1)
print(list1[0])
print(list1[-1])
for i in list1[:2]:
    print(i)
del list1[3:]
print(list1)