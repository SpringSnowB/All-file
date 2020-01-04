from flask import Flask,url_for

#将当前的模块构建成flask应用
#当前flask应用构建完成后就可以接收请求并给出响应
app=Flask(__name__)

# @app.route('/')#匹配当前服务器的根路径
# @app.route('/index')#可以用多个路由装饰器
# def index_view():
#     return 'this is the first index of flask'

@app.route('/')
@app.route('/index')
@app.route('/<int:number>')
def show_x(number=1):  #视图函数名不能重复
    if number!=1 :
        return '这是flask的第%s页'%number
    return '这是flask的首页'

@app.route('/mil')
def mil_vire():
    return 'this is web about mil'

@app.route('/show/<name>/<int:age>')
def show_view(name,age):
    # return 'welcome %s'%name
    print(type(name))
    print(type(age))
    myurl = url_for('show_view',name='pp',age=12)
    # return 'name:%s,age:%d'%(name,age)
    return '当前函数的访问路径是%s'%myurl

#在页面上显示日期
@app.route('/birthday/<int:year>/<int:month>/<int:day>')
def show_birthday(year,month,day):
    return "your birthday is %s-%s-%s"%(year,month,day)

if __name__=='__main__':
    # run(host = None,port = None,debug = None)
    app.run(debug=True)  #http://127.0.0.1:5000/当前参数的默认地址

