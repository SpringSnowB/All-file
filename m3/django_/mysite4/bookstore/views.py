from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Book
import decimal


def add_view(request):
    if request.method =='GET':
        return render(request,'bookstore/add.html')
    elif request.method == 'POST':
        title = request.POST['title']
        pub = request.POST['pub']
        if not title:
            return HttpResponse('please give me title')
        try:
            price = float(request.POST['price'])
            market_price = float(request.POST['market_price'])
        except Exception as e:
            print(e)
            return HttpResponse('your price is not number')
        #返回值QuerySet->[obj]

        #1,先从缓存拿flter的数据，缓存没有上几乎句
        # 2,查完数据的数据 记得存储到Cache里面一份
        all_book = Book.objects.filter(title=title)
        if all_book:

            return HttpResponseRedirect('书已存在')
        #返回值为对象
        # try:
        #     all_book = Book.objects.get(title=title)
        # except Exception as e:
        #     pass

        try:
            Book.objects.create(title=title,pub=pub,price=price,market_price=market_price)
        except Exception as e:
            return HttpResponse('%s已存在'%title)
        return HttpResponseRedirect('bookstore/all_book.html')


def all_book(request):
    # books = Book.objects.values('id','title','pub','price','market_price','create_time')
    books = Book.objects.values()
    return render(request,'bookstore/all_book.html',locals())


def update_book(request,n):
    if request.method =='GET':
        book = Book.objects.filter(id=n,isActive=True)
        if not book:
            return HttpResponse('not fond')
        return render(request,'bookstore/update_book.html',locals())
    elif request.method=='POST':
        try:
            price = float(request.POST['price'])
            market_price = float(request.POST['market_price'])
        except Exception as e:
            print(e)
            return HttpResponse('please give me number!')
        book = Book.objects.get(id=int(n))
        if book.price != decimal.Decimal(price) or book.market_price != decimal.Decimal(market_price):
            book.price=price
            book.market_price=market_price
            book.save()
        return HttpResponseRedirect('/bookstore/all_book.html')
        # books = Book.objects.values()
        # return render(request,'bookstore/all_book.html',locals())

def delete_book(request,id):
    book = Book.objects.get(id=id)
    if book.isActive ==True:
        book.isActive = False
        book.save()
    return HttpResponseRedirect('/bookstore/all_book.html')