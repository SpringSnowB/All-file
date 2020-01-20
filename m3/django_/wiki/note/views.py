from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def check_logging(fn):
    def wrap(request, *args, **kwargs):
        #检查登录状态
        if 'username' not in request.session or 'uid' not in request.session:
            #判断一下Cookies的情况
            if 'username' not in request.COOKIES or 'uid' not in request.COOKIES:
                #确实是没登录 或者是　之前登录状态失效了
                print('----check login faild 302----')
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = request.COOKIES['username']
                request.session['uid'] = request.COOKIES['uid']

        return fn(request, *args, **kwargs)
    return wrap


# Create your views here.
@check_logging
def add_view(request):
    if request.method == 'GET':

        return render(request,'note/add.html')

    elif request.method == 'POST':

        return HttpResponse('--post note is ok')