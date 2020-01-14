""""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
def rectCover(number):
    if number == 0:
        return 0
    fn_2 =1
    fn_1 =1
    for i in range(number-1):
        fn = fn_1+fn_2
        fn_2 = fn_1
        fn_1 = fn
    return fn_1

print(rectCover(0))