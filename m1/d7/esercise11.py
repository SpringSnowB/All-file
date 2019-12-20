
def class_score(score):
    """
    功能：打印成绩等级
    :param score: 输入的成绩
    :return: 返回等级
    """
    if score >60 or score < 0:
        return "成绩有误！"
    if 90 <= score <= 100:  # score >= 90 and score <= 100
        return "优秀！"
    if score >= 80:
        return "良好！"
    if score >= 60:
        return "及格！"
    return "不及格！"

score = float(input("请输入成绩："))
print(class_score(score))