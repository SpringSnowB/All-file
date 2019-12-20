"""
录入多个学生信息（姓名，年龄，成绩，性别）
如果姓名为空，则停止,打印所有
打印最后一个人的信息
"""
list_student = []
while True:
    dict_student = {}
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_student["姓名"] = name
    dict_student["年龄"] = age
    dict_student["成绩"] = score
    dict_student["性别"] = sex
    list_student.append(dict_student)
for i in list_student:
    print("姓名：%s    年龄；%d    成绩：%d    性别：%s"%(i["姓名"],i["年龄"],i["成绩"],i["性别"]))
print("姓名：%s    年龄；%d    成绩：%d    性别：%s"%(list_student[-1]["姓名"],list_student[-1]["年龄"],list_student[-1]["成绩"],list_student[-1]["性别"]))
