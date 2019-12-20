"""
定义函数，获取全局变量list01中所有偶数
使用传统思想
使用生成器思想

"""
list_number = [2,4,2,1,24,23,45,75,64]


def get_double():
    list_result = [item for item in list_number if item % 2 ==0]
    return list_result
print(get_double())



def get_even():
    for item in list_number:
        if item % 2 ==0:
            yield item
for item in get_even():
    print(item)