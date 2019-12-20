"""

"""
class Student:
    def __init__(self,name,age,sex,score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score
    def print_student_info(self):
        print("学生%s 年龄%d 性别%s 成绩%d"%(self.name,self.age,self.sex,self.score))

list_student = [
    Student("xxx",27,"f",100),
    Student("FFF",30,"f",60),
    Student("kkk",30,"f",70),
    Student("ggg",30,"m",85)
]

def find_student_with_name(name):
    for i in range(len(list_student)):
        if list_student[i].name == name:
            list_student[i].print_student_info()


find_student_with_name("xx")


def find_student_with_score(score):
    for i in range(len(list_student)):
        if list_student[i].score > score:
            list_student[i].print_student_info()

find_student_with_score(80)
def find_student_with_age(age):
    for item in list_student:
        if item.age > age:
            print(item.name)

find_student_with_age(12)

def find_student_score_is_min():
    min_score = list_student[0].score
    min_index = 0
    for i in range(len(list_student)):
        if min_score > list_student[i].score:
            min_score = list_student[i].score
            min_index = i
    list_student[min_index].print_student_info()

find_student_score_is_min()

def up_sort_score():
    for i in range(len(list_student)-1):
        for j in range(i+1,len(list_student)):
            if list_student[i].score > list_student[j].score:
                list_student[i],list_student[j] = list_student[j],list_student[i]

up_sort_score()
for item in list_student:
    item.print_student_info()
    print("---------")



def delete_man():
    for i in range(len(list_student)-1,-1,-1):
        if list_student[i].sex =="m":
            del list_student[i]

delete_man()
find_student_with_name("ggg")