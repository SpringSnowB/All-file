"""
business logic layer 业务逻辑层
"""
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
