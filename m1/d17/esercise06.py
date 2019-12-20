"""
获取list01中大于10的整数
"""
list01 = [1,2,"a",True,13]
# 生成器表达式
for item in (item for item in list01 if type(item)==int and item > 10):
    print(item)

# 生成器函数
def get_number():
    for item in list01:
        if type(item)==int and item > 10:
            yield item

for item in get_number():
    print(item)