"""
创建学生类（姓名、年龄、成绩）
直接将学生对象输出到终端
print(学生对象)-->我是%s，今年%d岁，成绩%d分
将学生对象克隆一份，改变其中一个对象，打印另外一个对象信息
"""
class Student:
    def __init__(self, name="", age=0, score=0):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "我是%s，今年%d岁，成绩%d分"%(self.name,self.age,self.score)
    def __repr__(self):
        return 'Student("%s",%d,%d)'%(self.name,self.age,self.score)

stu01 = Student("xx",22,89)
print(stu01)
stu02 = Student("SS",21,78)
stu03 = eval(stu02.__repr__())
print(stu03)
stu02.name = "jj"
print(stu02)