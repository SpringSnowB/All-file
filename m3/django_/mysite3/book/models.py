from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField('书名',max_length=11,null=False,unique=True)
    # 00000.00
    price = models.DecimalField('定价',max_digits=7,decimal_places=2)
    # descript = models.CharField('描述',max_length=50,default='')
    pub = models.CharField('出版社',max_length=30,null=False,default='')
    market_price = models.DecimalField('图书零售价',max_digits=7,decimal_places=2,default=0)

class Author(models.Model):
    name = models.CharField('姓名',max_length=20,null=False)
    age = models.IntegerField('年龄',null=False,default=1)
    email = models.EmailField('邮箱',null=True)
