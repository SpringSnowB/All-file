"""
录入多个学生信息（姓名，年龄，成绩，性别）
如果姓名为空，则停止,打印所有
如果录入“xx”,则单独打印其信息
"""
dict_student = {}
while True:
    student_name = input("请输入姓名：")
    if student_name != "":
        dict_student[student_name] = list(input("请输入该生信息：").split(" "))
    else:
        break
for k,v in dict_student.items():
    print("姓名：%s，年龄：%s,成绩:%s，性别：%s"%(k,v[0],v[1],v[2]))
if "xx" in dict_student.keys():
    print(dict_student["xx"])