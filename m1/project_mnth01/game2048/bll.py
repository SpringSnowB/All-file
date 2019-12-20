import random

class GameController:
    """
    游戏核心算法
    """
    def __init__(self):
        self.__list_merge = [2,0,2,0]
        self.__list_map = [
                        [2,0,2,0],
                        [2,4,0,2],
                        [0,0,2,0],
                        [2,4,4,2]
                            ]
        self.__list_index = []

    def __move_zero(self):
        """    零元素移动到末尾
        """
        while self.__list_merge[0] == 0:
            for i in range(len(self.__list_merge) - 1):
                if self.__list_merge[i] == 0:
                    self.__list_merge[i], self.__list_merge[i + 1] = self.__list_merge[i + 1], self.__list_merge[i]
        else:
            for i in range(len(self.__list_merge) - 1):
                if self.__list_merge[i] == 0:
                    self.__list_merge[i], self.__list_merge[i + 1] = self.__list_merge[i + 1], self.__list_merge[i]

    def __merge_same_element(self):
        """
        合并相同元素
        """
        self.__move_zero()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i+ 1] += self.__list_merge[i]
                self.__list_merge[i] = 0
        self.__move_zero()

    def left_move(self):
        """
        左移
        """
        for i in range(len(self.__list_map)):
            self.__list_merge = self.__list_map[i]
            self.__merge_same_element()

    def right_move(self):
        """
        右移
        """
        for i in range(len(self.__list_map)):
            self.__list_merge[:] = self.__list_map[i][::-1]
            self.__merge_same_element()
            self.__list_map[i][::-1] = self.__list_merge[:]

    def __transposition_matrix(self):
        for r in range(len(self.__list_map)):
            for c in range(r):
                if r != c:
                    self.__list_map[r][c], self.__list_map[c][r] = self.__list_map[c][r], self.__list_map[r][c]

    def up_move(self):
        self.__transposition_matrix()
        self.left_move()
        self.__transposition_matrix()

    def down_move(self):
        self.__transposition_matrix()
        self.right_move()
        self.__transposition_matrix()

    def __find_zero(self):
        for i in range(len(self.__list_map)):
            for j in range(len(self.__list_map[i])):
                if self.__list_map[i][j] == 0:
                    self.__list_index.append((i,j))#写成类，提高代码的可读性

    def product_number(self):
        self.__list_index.clear()
        self.__find_zero()
        number_index = random.randint(0,len(self.__list_index))
        number_probability = random.randint(1,11)
        if number_probability == 1:
            self.__list_map[self.__list_index[number_index][0]][self.__list_index[number_index][1]] =4
        else:
            self.__list_map[self.__list_index[number_index][0]][self.__list_index[number_index][1]] =2

    def __find_same_level(self):
        for line in self.__list_map:
            for i in range(len(line)-1):
                if line[i] == line[i+1]:
                    return False
        return True

    def __find_same_vertical(self):
        self.__transposition_matrix()
        result = self.__find_same_level()
        self.__transposition_matrix()
        return result

    def __find_same(self):
        result_level = self.__find_same_level()
        result_vertical = self.__find_same_vertical()
        return True if result_level and result_vertical else False

    def judge_game_over(self):
        """

        :return: True 表示游戏结束
        """
        self.left_move()
        if len(self.__list_index) and self.__find_same():
            return True
        else:
            return False