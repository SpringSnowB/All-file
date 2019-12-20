"""
my_zip
"""
def my_zip(iterable01,iterable02):
    if len(iterable01)<=len(iterable02):
        for i in range(len(iterable01)):
            yield (iterable01[i],iterable02[i])
    else:
        for i in range(len(iterable02)):
            yield (iterable01[i],iterable02[i])

list01 = ["a","b","c","v","m","o"]
list02 = [1,2,3,54,6]
for item in my_zip(list01,list02):
    print(item)