"""
循环计数
输出0 1 2 3
输出 2 4 6 8 10
输出 1 4 7 10
输出 8 7 6 5
输出-1 -2 -3 -4 -5
"""
count = 0
while count < 4:
    print(count)
    count +=1

count = 2
while count < 11:
    print(count)
    count +=2

count = 1
while count < 11:
    print(count)
    count +=3

count = 8
while count > 4:
    print(count)
    count -=1

count = -1
while count > -6:
    print(count)
    count -=1