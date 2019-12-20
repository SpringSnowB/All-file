"""
    创建函数，生成指定行数的杨辉三角。
    杨辉三角：
    每行端点与结尾的数为1，每个数是它左上方和右上方的数的和
    输入：6
    输出：
         [
                    [1],
                   [1, 1],
                  [1, 2, 1],
                 [1, 3, 3, 1],
               [1, 4, 6, 4, 1],
             [1, 5, 10, 10, 5, 1]
         ]
"""


def pascal_triangle(row):
    list_triangle = []
    for r in range(row):
        line = [None] *(r+1)
        line[0],line[-1] = 1,1
        for i in range(1,r):
            line[i] = list_triangle[r-1][i-1]+list_triangle[r-1][i]
        list_triangle.append(line)
    print(list_triangle)


pascal_triangle(6)

