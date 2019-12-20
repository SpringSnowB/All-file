"""
for index,item in my_enumerate(）
    print(index,item)
"""
dict01 = {"a":1,"b":2,"c":3}
list01 = [1,2,3,4,5,6]
def my_enumerate(vessel):
    index = 0
    for item in vessel:
        yield (index,item)
        index += 1

for index ,item in my_enumerate(list01):
    print(index,item)
