"""
数据逻辑层
"""
class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.sid = sid
        self.name = name
        self.age = age
        self.score =score
