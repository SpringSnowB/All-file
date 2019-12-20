"""
    学生管理系统

    一）
    数据模型类：StudentModel
		数据：编号 id,姓名 name,年龄 age,成绩 score
	逻辑控制类：StudentManagerController
		数据：学生列表 __stu_list
		行为：获取列表 stu_list,添加学生 add_student
	二）
	删除学生remove_student(stu_id)
	三）
	修改学生uodate_student(stu)
	四）
	根据学生成绩升序排序 order_by_score
	五）
	录入学生信息  __input_students
	六）
	输出学生信息  __display_student
	删除学生信息  __remove_student
	七）
	修改学生信息  __uodate_student
	根据学生成绩升序显示 __order_by_score
"""
class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.sid = sid
        self.name = name
        self.age = age
        self.score =score

class StudentManagerController:
    init_id = 191000
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stu_target):
        """
        添加学生
        :param 学生列表
        :return:
        """
        self.__generate_id(stu_target)
        self.stu_list.append(stu_target)

    def __generate_id(self, stu_target):
        """
        生成学生id
        """
        StudentManagerController.init_id += 1
        stu_target.sid = self.init_id

    def remove_student(self,stu_id):
        for item in self.__stu_list:
            if item.sid == stu_id:
                self.__stu_list.remove(item)
                return True
        else:
            return False

    def update_student(self,update_stu):
        for item in self.__stu_list:
            if item.sid == update_stu.sid:
                item.age,item.score, item.name= update_stu.age,update_stu.score,update_stu.name
                return True
            else:
                return False

    def order_by_score(self):
        for i in range(len(self.stu_list)-1):
            for j in range(i+1,len(self.stu_list)):
                if self.stu_list[i].score > self.stu_list[j].score:
                    self.stu_list[i],self.stu_list[j]=self.stu_list[j],self.stu_list[i]

    def display_student(self):
        for item in self.stu_list:
            print(item.sid,item.name,item.age,item.score)

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

    def __select_menu(self):
        while True:
            self.__display_menu()
            select = int(input())
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
                print("输入错误,请重新输入。")

    def __input_students(self):

        while True:
            stu = StudentModel()
            stu.name = input("请输入姓名：")
            if stu.name == "":
                break
            stu.age = int(input("请输入年龄："))
            stu.score = int(input("请输入成绩："))
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


view = StudentManagerView()
view.main()

# #-----------------------
# # 测试
# manager = StudentManagerController()
#
# stu = StudentModel("悟空",28,100)
# stu2 = StudentModel("bajie",28,100)
#
# manager.add_student(stu)
# manager.add_student(stu2)
#
# re = manager.update_student(StudentModel("悟空",29,90,191001))
# stu3=StudentModel("shas",29,60)
# stu4=StudentModel("shs",29,70)
# manager.add_student(stu3)
# manager.add_student(stu4)
# print(re)
# manager.order_by_score()
#
# for item in manager.stu_list:
#     print(item.sid,item.name,item.score,item.age)
#
#
# print(manager.remove_student(191002))
# print(manager.remove_student(191002))
# # for item in manager.stu_list:
# #     print(item.sid,item.name)