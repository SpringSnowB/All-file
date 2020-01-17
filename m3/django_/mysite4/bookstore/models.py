from django.db import models

# Create your models here.
class Book(models.Model):
    # 初始化表时，不强制指定默认值，但是新增字段时，由于字段默认为非空，所以必须制定default，从而避免无法赋值问题
    title = models.CharField('书名',max_length=11,unique=True)
    pub = models.CharField('出版社',max_length=50)
    price = models.DecimalField('定价',max_digits=7,decimal_places=2)
    market_price = models.DecimalField('零售价',max_digits=7,decimal_places=2)
    # auto_now_add:新增数据时 django自动将当前时间更新到该字段中
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    # auto_now:每次更新数据时，django自动将当前时间更新到该字段中
    update_time = models.DateTimeField('更新时间',auto_now=True)
    isActive = models.BooleanField('是否活跃',default=True)

    def __str__(self):
        #定义类实例化后的对象的输出格式
        return 'title:%s pub:%s price:%s market_price:%s'%(self.title,self.pub,self.price,self.market_price)