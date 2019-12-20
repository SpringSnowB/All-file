"""
矩阵转置
"""
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

for r in range(len(list01)):
    for c in range(r):
        if r != c:
            list01[r][c],list01[c][r] = list01[c][r],list01[r][c]
print(list01)
