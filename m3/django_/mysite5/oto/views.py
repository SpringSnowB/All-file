from django.http import HttpResponse
from django.shortcuts import render
from .models import Author,Wife

# Create your views here.
def test_oto(request):
    #创建数据
    #Author Wife[有外键--属性名author--外键字段名author_id]
    #方案1
    # author = Author.objects.create(aname = '章正月')
    # wife = Wife.objects.create(wname = '露露',author=author)
    #方案2
    author = Author.objects.create(aname='唐家三少')
    wife = Wife.objects.create(wname='窝窝',author_id=author.id)

    #查询
    #Author Wife[有外键--属性名author--外键字段名author_id]
    #正向 wife -->Author
    w1 = Wife.objects.get(id=1)
    a1 = Author.objects.get(id=2)
    return HttpResponse('wo0O~~~%s ---%s||||%s----%s'%(w1.wname,w1.author.aname,a1.aname,a1.wife.wname))