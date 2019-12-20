"""
定义函数,返回列表中不重复的元素(顺序不重要)
"""
def return_no_repetition(list_input):
    return [item for item in list_input if list_input.count(item) == 1]

def return_no_repetition(list_input):
    return list(set(list_input))

print(return_no_repetition([4,35,7,64,7,35]))

