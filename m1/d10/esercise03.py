"""
在终端中循环录入学生信息（名字、年龄、性别、成绩）
"""
class Student:
    def __init__(self,name,age,sex,score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score
    def print_student_info(self):
        print("学生%s 年龄%d 性别%s 成绩%d"%(self.name,self.age,self.sex,self.score))
list_student = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = int(input("请输入学生年龄："))
    sex = input("请输入学生性别：")
    score = int(input("请输入学生成绩："))
    student = Student(name,age,sex,score)
    list_student.append(student)

for item in list_student:
    item.print_student_info()