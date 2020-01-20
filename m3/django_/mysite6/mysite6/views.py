from django.http import HttpResponse


def set_cookie(request):
    #设置Cookies, 在响应头中添加特殊响应头　Set-Cookie ,浏览器接到该响应头后，自动将值存储到本地浏览器的Cookies区域
    res = HttpResponse('---set cookies')
    res.set_cookie('username', 'guoxiaonao',max_age=300)

    #删除Cookies
    #res.delete_cookie('username')

    return res


def get_cookie(request):
    #类字典对象
    username = request.COOKIES.get('username', 'no user')
    return HttpResponse('username is %s'%(username))


def set_session(request):
    #存储session
    request.session['username'] = 'guoxiaonao'

    #删除session中的数据
    #del request.session['username']

    return HttpResponse('--set session is ok')

def get_session(request):

    username = request.session['username']
    return HttpResponse('--get session is ok username is %s'%(username))

























