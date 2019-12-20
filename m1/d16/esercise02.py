"""
使用迭代器思想，获取元组/字典中所有元素
"""
# tuple01 = ("a","b","c")
# iterator = tuple01.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
dict01 = {"a":1,"b":2,"c":3}
iterator_key = dict01.keys().__iter__()
iterator_value = dict01.values().__iter__()
while True:
    try:
        key = iterator_key.__next__()
        value = iterator_value.__next__()
        print("%s:%d"%(key,value))
    except StopIteration:
        break