from django.db import models

# Create your models here.

class Publisher(models.Model):
    # 出版社 1
    pname = models.CharField(max_length=11,verbose_name='名字')
    # 隐式属性 book_set

    def __str__(self):
        return '%s'%self.pname


class Book(models.Model):
    #图书  m
    bname = models.CharField(max_length=11,verbose_name='书名')
    publisher = models.ForeignKey(Publisher)


    def __str__(self):
        return '%s--->%s'%(self.bname,self.publisher)