"""
定义一个函数，获取成绩0--100
"""
def get_score():
    while True:
        try:
            score = int(input("请输入成绩："))
        except:
            print("请输入整数")
        else:
            if score in range(0,101):
                return score
score = get_score()
print(score)




