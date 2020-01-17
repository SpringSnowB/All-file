from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名',max_length=11)
    age = models.IntegerField('年龄')
    desc = models.CharField('个人描述',max_length=50)


    def __str__(self):

        return '%s'%(self.name)

    class Meta:
        # 更改该类对应的表名
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name