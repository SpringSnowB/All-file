from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User

# Create your views here.
def reg_view(request):
    #注册
    if request.method == 'GET':
        return render(request,'user/register.html')
    elif request.method == 'POST':
        #处理注册数据
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        #TODO 数据是否提交　验证

        if password_1 != password_2:
            password_error = 'Your passwords is not same~'
            return render(request, 'user/register.html',locals())

        #明文 -> 散列
        # hash算法　->
        # 1, 不可逆　2, 定长输出［不管输入多长，结果的长度都是恒定的；具体长度根据您挑选的算法为准，例如md5为32位16进制］3, 雪崩效应［文件的完整性校验］
        import hashlib
        #生成hash算法的计算对象
        m = hashlib.md5()
        #将要计算的明文传至计算对象 [参数为字节串]
        m.update(password_1.encode())
        #计算对象.hexdigest -> 获取16进制结果
        m_password = m.hexdigest()

        #当前用户名是否已注册
        old_users = User.objects.filter(username=username)
        if old_users:
            error = 'The username is already existed'
            return render(request, 'user/register.html',locals())

        try:
            user = User.objects.create(username=username, password=m_password)
        except Exception as e:
            print('--create is error')
            print(e)
            error = 'The username is already existed!'
            return render(request, 'user/register.html', locals())

        #免登陆一天
        request.session['username'] = username
        request.session['uid'] = user.id

        return HttpResponse('---register is ok')


def login(request):

    if request.method == 'GET':
        #如果用户已经登陆了，　直接显示字符串　已登录
        #1,先判断session中是否有值，有值是已登录
        if 'username' in request.session and 'uid' in request.session:
            return HttpResponse('--大哥　您已经登陆过了')
        #2,session无值时，再检查一下Cookies中是否有值，如果有值，回写session,已登录～
        if 'username' in request.COOKIES and 'uid' in request.COOKIES:
            #回写session
            request.session['username'] = request.COOKIES['username']
            request.session['uid'] = request.COOKIES['uid']
            return HttpResponse('--大哥　您已经登陆过了　！')

        #用户未登录时，才能显示html
        return render(request, 'user/login.html')

    elif request.method == 'POST':
        #处理登录的数据
        #用户名和密码的匹配
        username = request.POST.get('username')
        password = request.POST.get('password')

        old_users = User.objects.filter(username=username)
        if not old_users:
            error = 'Your username or password is error!'
            return render(request, 'user/login.html', locals())
        old_user = old_users[0]
        #将用户提交的密码　再次做md5计算，将新计算的结果与数据库中的密码进行比对，如果不一致，则为密码错误
        import hashlib
        m = hashlib.md5()
        m.update(password.encode())
        m_password = m.hexdigest()

        if m_password != old_user.password:
            error = 'Your username or password is wrong !'
            return render(request, 'user/login.html',locals())

        #session
        request.session['uid'] = old_user.id
        request.session['username'] = username

        resp = HttpResponse('---login is ok')
        #检查是否需要存储Cookies
        #检查用户是否　勾选了　'记住用户名',如果勾选，还需要在Cookies中存储　uid&username 过期时间为７天
        if 'isSaved' in request.POST.keys():
            #用户勾选了　记住用户名　存Cookies
            resp.set_cookie('uid', old_user.id, 60*60*24*7)
            resp.set_cookie('username',username,60*60*24*7)

        return resp

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    resp = HttpResponseRedirect('/')
    if 'username' in request.COOKIES:
        del request.COOKIES['username']
    if 'uid' in request.COOKIES:
        del request.COOKIES['uid']
    return









