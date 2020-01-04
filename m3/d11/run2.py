from flask import Flask,render_template,request

#修改默认的模板目录位置  templates--->t
#报错  jinja2.exceptions.TemplateNotFound: index.html
app= Flask(__name__,template_folder='t')

@app.route('/')
def index_view():
    #通过render_template函数渲染模板
    name = 'qtx'
    age = 19
    eamil = 'qjoiw@163.com'
    address = 'jdajajj'
    phone = '123324'

    mylist=[
        {
            'id':1,
            'content':'love studying'
        },
        {
            'id':2,
            'content':'full in studying'
        },
        {
            'id':3,
            'content':'lalalallalal'
        },
        {
            'id':4,
            'content':'babababab'
        }
    ]

    # return render_template('index.html',name='qq',age=18)
    
    # return render_template('index.html',context= locals())
    #locals收集局部变量保存在字典中
    return render_template('index.html',**locals())

    #当用户访问/user/login 能看见登录页面login.html
@app.route('/user/login')

def login_view():
    print(request.args)
    uname = request.args.get('uname')
    pwd = request.args.get('password')
    print(uname,pwd)
    return render_template('login.html',**locals())

if __name__=='__main__':
    app.run(debug=True)