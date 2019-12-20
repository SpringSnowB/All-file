"""
随机生成由大写字母、小写字母、数字组成的四位验证码
"""
import random

def produce_number():
    return str(random.randint(0,9))

def produce_big_word():
    return chr(random.randint(65,90))

def produce_small_word():
    return chr(random.randint(97,112))

def produce_varification_code():
    s = ''
    func_tuple = (produce_number,produce_big_word,produce_small_word)
    for i in range(4):
        func_num = random.randint(0,2)
        s += func_tuple[func_num]()
    return s