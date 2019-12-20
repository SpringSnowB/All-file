"""
print("*",end= " ")
end 参数默认换行
循环嵌套
"""

for i in range(6):
    for j in range(4):
        if i % 2 !=0:
            print("#",end="")
        else:
            print("*",end="")
    print("")