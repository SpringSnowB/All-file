"""
优秀 良好 及格 不及格 成绩有误

"""
score = float(input("请输入成绩："))
if 90 <= score <= 100: #score >= 90 and score <= 100
    print("优秀！")
elif score >= 80:
    print("良好！")
elif score >= 60:
    print("及格！")
elif 0 <= score < 60:
    print("不及格！")
else:
    print("成绩有误！")
# 范围最广的先行判断，之后从小到大或从大到小判断