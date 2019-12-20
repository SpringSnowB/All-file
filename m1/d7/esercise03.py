"""
打印二维列表第三行数据，一行一个

"""
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
for i in list01[2]:
    print(i)

print(len(list01[:1]))

for r in range(len(list01)):
    print(list01[r][1])

for r in range(len(list01)):
    for c in list01[r]:
        print(c,end="\t")
    print()

for r in range(len(list01)-1,-1,-1):
    print(list01[r][2])

for c in range(len(list01)-1,-1,-1):
    print(list01[3][c])