from flask import Flask,render_template,request

app = Flask(__name__,'/static')

@app.route('/index')
@app.route("/")
def index_view():
    return render_template('index.html')#接收一个模板页来响应浏览器

#路由函数默认只接收get请求  methods=['get','post']表示当前视图函数可以接收get和post请求
@app.route('/user/login',methods=['get','post'])
def login_view():
    # 接收form表单get请求提交的数据
    #从前端获取input name = 'uname'的值
    # uname = request.args.get('uname')
    # pwd = request.args.get('pwd')

    #接收表单post提交的数据
    print(request.form)#类似字典的对象
    uname = request.form.get('uname')
    pwd = request.form.get('pwd')
    #验证登录...
    return "欢迎您，%s"%uname

@app.route('/xhr')
def xhr_view():
    return render_template('xhr.html')
@app.route('/getServer')
def get_server_view():
    uname = request.args.get('uname')
    if request.args.get('uname'):
        return '欢迎%s'%uname
    return '接收AJAX get请求成功'
@app.route('/01/get')
def get_01_view():
    return render_template('ajax-get.html')

@app.route('/calcSever')
def calc_view():
    # 如果是get请求时
    if request.method=='GET':
        if request.args:
            num1 = request.args.get('num1')
            num2 = request.args.get('num2')
            opt = request.args.get('opt')
            if opt == '1':
                return '计算结果是：%d' %(int(num1)+int(num2))
            elif opt == '0':
                return '计算结果是：%d' % (int(num1)-int(num2))
        else:
            return render_template('calc.html')
    # 如果有数据 处理get请求提交的数据
    # 如果没有数据 显示页面calc.html
    # 如果是post请求 其他扩展

@app.route('/postServer',methods=['get','post'])
def server_post():
    if request.method=='GET':
        return render_template('ajax-post.html')
    elif request.method=='POST':
        print(request.form)
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        print(name,age,email)
        return 'xxxxx'
if __name__ == '__main__':
    app.run(debug=True)