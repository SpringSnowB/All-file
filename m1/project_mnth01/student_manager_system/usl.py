"""
user show layer 用户显示层
"""
from project_mnth01.student_manager_system.bll import StudentManagerController
from project_mnth01.student_manager_system.model import StudentModel
class StudentManagerView:
    """
    视图
    """
    def __init__(self):
        self.__manager = StudentManagerController()

    def main(self):
        self.__display_student()
        self.__select_menu()

    def __display_menu(self):
        print("1.添加学生")
        print("2.显示学生")
        print("3.删除学生")
        print("4.修改学生")
        print("5.根据成绩升序显示学生")
        print("6.退出")
    def __input_error(self,string = ""):
        while True:
            try:
                input_data = int(input(string))
                return input_data
            except:
                print("输入有误，请重新输入")

    def __select_menu(self):
        while True:
            self.__display_menu()
            select = self.__input_error("请输入选择")
            if select == 1:
                self.__input_students()
            elif select == 2:
                self.__display_student()
            elif select ==3:
                self.__remove_student()
            elif select == 4:
                self.__update_student()
            elif select ==5:
                 self.__order_by_score()
            elif select ==6:
                break
            else:
                pass

    def __input_students(self):

        while True:
            stu = StudentModel()
            stu.name = input("请输入姓名：")
            if stu.name == "":
                break
            stu.age = self.__input_error("请输入年龄")
            stu.score = self.__input_error("请输入成绩")
            self.__manager.add_student(stu)

    def __update_student(self):
        stu = StudentModel()
        stu.name = input("请输入姓名：")
        stu.age = int(input("请输入年龄："))
        stu.score = int(input("请输入成绩："))
        stu.sid = int(input("请输入编号："))
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __remove_student(self):
        sid = int(input("请输入编号："))
        self.__manager.remove_student(sid)

    def __order_by_score(self):
        self.__manager.order_by_score()
        self.__display_student()

    def __display_student(self):
        self.__manager.display_student()
