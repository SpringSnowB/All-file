import time

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(30)#方案1
def test_cache(request):
    # time.sleep(3)

    #缓存 方案2
    # res = Book.objects.filter()
    # cache.set('key1','res',30)
    #先尝试拿缓存里的数据，如果有，就不要再查询数据
    #c_res = cache.get('key1')
    print('-----start view-----')
    return HttpResponse('hello')

def test_template_cache(request):

    return  render(request,'test_template.html',locals())


def test(request):
    return HttpResponse('this is test')

def test_csrf(request):

    return render(request,'test_csrf.html')