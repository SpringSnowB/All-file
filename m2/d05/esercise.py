"""
求100000以内的质数
"""
from time import time
def print_time(func):
    def wrapper(*args,**kwargs):
        star = time()
        re = func(*args,**kwargs)
        end = time()
        print(end - star)
        return re
    return wrapper



def find(star_number,end_number):
    for i in range(star_number,end_number+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            yield i

@print_time
def count_number(star_number=1,end_number=100000):
    count = 0
    for item in find(star_number,end_number):
        count += item
    return count

result = count_number(1,100000)
print(result)


