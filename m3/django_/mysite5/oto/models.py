from django.db import models

# Create your models here.

class Author(models.Model):
    aname = models.CharField('姓名',max_length=11)
    #隐式类属性 对面类名小写 -- wife


#有外键属性的一方 查询另一方 为正向查询 wife -->author为正向查询   author-->wife为反向查询
class Wife(models.Model):
    wname = models.CharField('姓名',max_length=11)
    author = models.OneToOneField(Author)