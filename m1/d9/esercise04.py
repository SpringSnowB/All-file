"""
    质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
    定义函数，获取指定范围内的所有质数。
    输入：2,20
    输出：[2, 3, 5, 7, 11, 13, 17, 19]
    提示:判断9是否为质数
       从2 --- 8开始逐一判断,是否能被9整除,如果能则不是
"""
def is_prime(number):
    for i in range(2,number):
        if number % i ==0:
            return False
    return True

def find_prime_number(start,end):
    list_result = []
    for number in range(start,end):
        if is_prime(number):
            list_result.append(number)

    return list_result

print(find_prime_number(3,29))