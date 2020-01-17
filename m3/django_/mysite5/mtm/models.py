from django.db import models

# Create your models here.
class Author(models.Model):

    aname = models.CharField('姓名',max_length=11)


    def __str__(self):
        return self.aname


class Book(models.Model):
    bname = models.CharField('书名',max_length=11)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.bname