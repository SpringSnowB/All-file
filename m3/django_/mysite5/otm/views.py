from django.http import HttpResponse
from django.shortcuts import render
from .models import Publisher,Book

# Create your views here.
def test_otm(request):

    #创建数据
    # pub = Publisher.objects.create(pname = '清华大学出版社')
    # book = Book.objects.create(bname = 'Python高级',publisher = pub)
    # book2 = Book.objects.create(bname = 'Python Web',publisher_id=pub.id)

    #查询
    #正向 多查一  Book-->Pub
    book = Book.objects.get(id=1)
    print("正向"+book.bname+":"+book.publisher.pname)
    #反向  一查多  Pub -- >Book
    pub = Publisher.objects.get(id=1)
    # print(type(pub.book_set))
    print("反向\n"+pub.pname)
    print(pub.book_set.all())


    return HttpResponse('ooooWWWW`')