from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

post_form = """
<form method='post' action="/test_post">
    姓名:<input type="text" name="username">
    密码:<input type="text" name="pwd">
    <input type='submit' value='登陆'>
</form>
"""

def test_post(request):
    if request.method == 'GET':
        # 返回html
        return HttpResponse(post_form)
    elif request.method == 'POST':
        # 处理提交上来的数据
        #form post提交时 请求头中的Content-Type:application/x-www-form-urlencoded
        # request.POST 只能针对于post提交格式为表单提交的数据

        #默认django开启post请求中的csrf防御，如果不符合防御要求，post提交会被禁止，返回403：可禁止

        #text框 空提交时，浏览器会将text框的name提交至服务器，但值为空
        username = request.POST['username']
        # return HttpResponse('welcome %s'%username)
        #302 跳转 参数跳转的具体地址  --相对地址

        #浏览器如何知道  要跳转以及跳转到哪里去？
        #1,响应码302告知浏览器   需要进行地址栏跳转  2,302响应一定会有一个Locatiob响应头，其值为服务器希望用户跳转到的地址
        return HttpResponseRedirect('/index')

def index_view(request):
    return HttpResponse('index')

def test_tempaltes(request):
    # 方案一
    # #通过loader加载模板
    # t = loader.get_template('test_templates.html')
    # #将t转换成HTML字符串
    # html = t.render()
    # return HttpResponse(html)

    # 方案二
    #模板传参 一定是字典
    dic = {'username':'pp','age':'20'}
    return render(request,'test_templates.html',dic)

def say_hi():
    return 'hi everybody'

def test_params(request):
    dic = {}
    dic['str']='pp'
    dic['int']=30
    dic['list'] = ['pp','ee']
    dic['dict'] = {'name':'uu','age':28}
    dic['say_hi'] = say_hi
    dic['class_obj'] = Dog()

    #xss攻击 后端防御xss可以执行 html.escape(str)
    dic['script'] = '<script>alert(111)</script>'
    return render(request,'test_params.html',dic)

class Dog:
    def say(self):
        return 'WOo wo~~~'

def test_if(request):
    dic = {'x':23}
    return render(request,'test_if.html',dic)

def calculate(request):
    if request.method=='GET':
        return render(request, 'calculate.html')
    elif request.method=='POST':
        try:
            x=int(request.POST['x'])
            op = request.POST['op']
            y = int(request.POST['y'])
        except Exception as e:
            print(e)
            return HttpResponse('please give me number')
        result = 0
        if op =='add':
            result = x+y
        elif op =='sub':
            result = x-y
        elif op =='mul':
            result = x*y
        elif op =='div':
            result = x/y
        # dic = {}
        # dic['result'] = result
        return render(request, 'calculate.html', locals())


def shebao(request):

    # GET vs POST
    # GET 查询 [管服务器要数据]
    # POST：向服务器提交数据/隐私数据的提交
    # form 提交 POST


    if request.method=='GET':
        return render(request,'shebao.html')
    elif request.method=='POST':
        try:
            base = int(request.POST['base'])
        except Exception as e:
            error = 'please give number!!!'
            return render(request,'shebao.html',locals())
        base = max(3082,min(base,23118))
        is_city = request.POST['is_city']
        yanglao_person = base*0.08
        yanglao_company = base*0.19
        shiye_person = base * 0.002 if is_city == '1' else 0
        shiye_company = base*0.008
        gongshang_person = 0
        gongshang_company = base*0.005
        shengyu_person = 0
        shengyu_company = base*0.008
        yiliao_person = base*0.002+3
        yiliao_company = base*0.01
        gongjijin = base*0.12
        sum_person = yanglao_person+shengyu_person+gongshang_person+shengyu_person+yiliao_person+gongjijin
        sum_company = yanglao_company+shengyu_company+gongshang_company+shengyu_company+yiliao_company+gongjijin
        cal = sum_company+shengyu_person
        return render(request,'shebao.html',locals())




