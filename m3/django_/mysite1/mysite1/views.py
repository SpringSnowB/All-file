from django.http import HttpResponse

def index_view(request):
    html = '<h1> this is index</h1>'
    return HttpResponse(html)

def page1_view(request):
    html = '<h1> This is first page</h1>'
    return HttpResponse(html)

def page2_view(request):
    html = '<h1> This is second page</h1>'
    return HttpResponse(html)

def pagen_view(request,n):
    html = "<h1> This is %sth page</h1>"%n
    return HttpResponse(html)

def acl_view(request,n,acl,m):
    if acl=='add':
        html = str(int(n)+int(m))
    elif acl =='sub':
        html = str(int(n)-int(m))
    elif acl =='mul':
        html = str(int(n)*int(m))
    else:
        html = "ERROR"
    return HttpResponse(html)

def person_view(request,name,age):
    html = '<h1>name:%s<br>age:%s</h1>'%(name,age)
    return HttpResponse(html)

def birthday_view(request,year,month,day):
    print(request.path_info)
    print(request.method)
    html = 'birthday is %s年%s月%s日'%(year,month,day)
    return HttpResponse(html)

def test_get(request):
    # 测试获取查询字符串的值
    print(dict(request.GET))
    # print(request.GET['a'])#默认打印最后一个值
    print(request.GET.get('a','abcdefg'))#如果没有a，则按次序向下找b c d e f g的值
    print(request.GET.getlist('a'))
    html = """
    <form method='get' action='/test_get_server'>
    姓名：<input type='text' name=''>
        <input type='submit' value='提交'>
    </form>
    """
    return HttpResponse(html)


def test_get_server(request):
    print(dict(request.GET))
    return HttpResponse('test get server is ok')