"""
练习，在不改变fun01与fun02函数定义和调用的情况下
为其增加新功能（打印函数执行时间）
"""

import time

def print_function_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        re = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time-start_time)
        return re
    return wrapper


@print_function_time
def fun01():
    time.sleep(2)#睡眠2秒，模拟计算2秒
@print_function_time
def fun02():
    time.sleep(3)

fun01()
fun02()