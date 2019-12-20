
list_one = [0,2,2,4]


def move_zero_to_end():
    """
    定义函数将0元素移动至末尾
    """
    for i in range(len(list_one)-1,-1,-1):
        if list_one[i] == 0:
            del list_one[i]
            list_one.append(0)
# move_zero_to_end()
# print(list_one)

def merge_same_element():
    """
    合并相同元素
    :return:
    """
    move_zero_to_end()
    for i in range(len(list_one)-1):
        if list_one[i] == list_one[i+1]:
            list_one[i] += list_one[i+1]
            del list_one[i+1]
            list_one.append(0)

# merge_same_element()
# print(list_one)

map = [
    [2, 0, 2, 0],
    [2, 4, 0, 2],
    [0, 0, 2, 0],
    [2, 4, 4, 2],
]

def left_move():
    """
    将二维列表的每一行进行左移动
    思想：每行交给merge_same_element()
    """
    global list_one
    for line in map:
        list_one = line
        merge_same_element()

# left_move()
# print(map)

def right_move():
    """
    将二维列表的每一行进行右移
    思想：倒序获取每行交给list_one,进行merge_same_element()
    """
    global list_one
    for line in map:
        list_one[:] = line[::-1]
        merge_same_element()
        line[:] = list_one[::-1]

# right_move()
# print(map)

def transposition_matrix():
    for row in range(len(map)):
        for column in range(row):
            if row != column:
                map[row][column],map[column][row] = map[column][row],map[row][column]

# transposition_matrix()
# print(map)

def up_move():
    """
    将每列元素向上移动
    思想：转置之后向左移动再转置回来
    """
    transposition_matrix()
    left_move()
    transposition_matrix()

# up_move()
# print(map)


def down_move():
    transposition_matrix()
    right_move()
    transposition_matrix()

down_move()
print(map)