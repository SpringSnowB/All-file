"""
随机加法考试
"""
import random
score = 0
for item in range(3):
    random_number1, random_number2 = random.randint(1,10), random.randint(1,10)
    # print(str(random_number1)+"+"+str(random_number2)+"= ?")
    number = int(input(str(random_number1)+"+"+str(random_number2)+"= ?"))
    if number == random_number1+random_number2:
        print("真棒")
        score += 10
    else:
        print("做错啦")
        score -= 5
print("您的最终得分是："+str(score))