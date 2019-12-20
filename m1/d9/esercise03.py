"""
    定义函数，返回字符串中第一个不重复的字符。
    输入：ABCACDBEFD
    输出：E
"""
def return_first_no_repetition(string):
    for item in string:
        if string.count(item) == 1:
            return item
    return "没有无重复字符"

print(return_first_no_repetition("ABCACDBEFDEF"))