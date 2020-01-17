from django.http import HttpResponse
from django.shortcuts import render
from .models import Author,Book

# Create your views here.

def test_mtm(request):
     #
     # author = Author.objects.create(aname='太宰治')
     # author2 = Author.objects.create(aname='太宰 治')
     # book = author.book_set.create(bname='人间失格')
     # author2.book_set.add(book)
     # book2 = author.book_set.create(bname='人间 失格')

     #正向 Book -->author
     b1 = Book.objects.get(id=1)
     print("正向："+b1.bname)
     print(b1.author.all())
     a1 = Author.objects.get(id=1)
     print("反向："+a1.aname)
     print(a1.book_set.all())

     return HttpResponse('mtm oooo~~~')