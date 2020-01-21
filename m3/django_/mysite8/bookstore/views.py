from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from bookstore.models import Book

# Create your views here.
def index_view(request):
    # 查询字符串上传 用户选择的 页码
    all_book = Book.objects.all()
    paginator = Paginator(all_book,2)

    cur_page = request.GET.get('page',1)
    try:
        page = paginator.page(cur_page)
    except Exception as e:
        return HttpResponse('----page is wrong----')
    return render(request,'book_index.html',locals())
