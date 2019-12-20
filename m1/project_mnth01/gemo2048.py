"""
2048 核心算法
"""
#1.定义函数，零元素移动到末尾
__list_merge = [0, 0, 2, 2]

def move_zero():
    """    零元素移动到末尾
    """
    while __list_merge[0] ==0:
        for i in range(len(__list_merge) - 1):
            if __list_merge[i] == 0:
                __list_merge[i], __list_merge[i + 1] = __list_merge[i + 1], __list_merge[i]
                # for j in range(i+1,len(list_merge)-1):
                #     list_merge[j-1],list_merge[j] = list_merge[j],list_merge[j-1]
    else:
        for i in range(len(__list_merge) - 1):
            if __list_merge[i] == 0:
                __list_merge[i], __list_merge[i + 1] = __list_merge[i + 1], __list_merge[i]
                # for j in range(i+1,len(list_merge)-1):
                #     list_merge[j-1],list_merge[j] = list_merge[j],list_merge[j-1]

def merge_same_element():
    """
    合并相同元素
    """
    move_zero()
    for i in range(len(__list_merge) - 1):
        if __list_merge[i] == __list_merge[i + 1]:
            __list_merge[i + 1] += __list_merge[i]
            __list_merge[i] = 0


move_zero()
merge_same_element()
print(__list_merge)

list_map = [
    [2,0,2,0],
    [2,4,0,2],
    [0,0,2,0],
    [2,4,4,2]
]


def left_move():
    """
    左移
    """
    for i in range(len(list_map)):
        global __list_merge
        list_merge = list_map[i]
        merge_same_element()

def right_move():
    """
    右移
    """
    for i in range(len(list_map)):
        __list_merge[:] = list_map[i][::-1]
        merge_same_element()
        list_map[i][::-1] = __list_merge[:]


def transposition_matrix():
    for r in range(len(list_map)):
        for c in range(r):
            if r != c:
                list_map[r][c], list_map[c][r] = list_map[c][r], list_map[r][c]


def up_move():
    transposition_matrix()
    left_move()
    transposition_matrix()

def down_move():
    transposition_matrix()
    right_move()
    transposition_matrix()

left_move()
print(list_map)
right_move()
print(list_map)
up_move()
print(list_map)
down_move()
print(list_map)