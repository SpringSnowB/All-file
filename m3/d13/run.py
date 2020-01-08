from flask import Flask,render_template,request,jsonify
import json

app = Flask(__name__)

@app.route('/reg')
def reg_view():
    return render_template('register.html')

@app.route('/check_uname')
def check_view():
    ulist = ['qq','pp','mm']
    #当前端get请求发送时，接收前端数据uname 判断是否在ulist中  在则返回用户名已存在，否则返回用户名可以使用
    if request.method=='GET':
        uname = request.args.get('uname')
        if uname in ulist:
            return '1'
        else:
            ulist.append(uname)
            return '0'

@app.route('/get_user')
def get_user():
    return render_template('get-user.html')

@app.route('/get_user_server')
def get_user_server():
    data = [
        {"id":'1','name':"Bob","pwd":'1213412'},
        {"id": '2', 'name': "Tom", "pwd": '12wq13412'},
        {"id": '3', 'name': "Horry", "pwd": '153g412'}
    ]
    # separator 默认(",",": ")带有多余的空格 sort_keys = True 对数据键进行排序
    # return json.dumps(data,separators=(',',":"),sort_keys=True)
    # return '1_Bob_12345|2_Tom_123454|3_Horry_1289u3'
    # id_uname_pwd|id_uname_pwd...

    return jsonify(data) #响应的是一个json的数据而json.dumps则是普通文本数据

@app.route('/post_json')
def post_json():
    return render_template('post-json.html')
@app.route('/post_json_server',methods=['get','post'])
def post_json_server():
    # uname = request.form.get('uname')
    json_str = request.get_json()
    # print(request.json)#同样可以获得json数据
    # print(json_str.get('uname'))#获取json内相关数据
    uname = json_str.get('uname')
    pwd = json_str.get('pwd')
    #登录失败对浏览器是正常的响应，但对程序逻辑来说是失败的操作 考虑自定义状态码 告诉前端目前程序的结果
    data = {"code":201,"msg":"登录失败"}
    if uname=='wang' and pwd =='123456':
        return jsonify({"code":200,"msg":"ok"}) 
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)
    app.config(False)