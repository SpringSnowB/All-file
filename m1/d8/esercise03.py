"""
统计函数被执行次数
"""
count = 0
def count_def():
    global count
    count += 1


count_def()
count_def()
count_def()
count_def()
count_def()

print(count)

