from flask import Flask,render_template,request,jsonify
import json
app=Flask(__name__)

@app.route('/load')
def load_view():
    return render_template('load_test.html')

@app.route('/load_server',methods=['get','post'])
def load_server_view():
    return render_template('load_test_server.html')


@app.route('/get')
def get_view():
    return render_template('jq-get.html')

@app.route('/get_server')
def get_server_view():
    uname = request.args.get('uname','not fond')#可以添加默认值
    age = request.args.get('age','not fond')
    s = 'name is %s,age is %s'%(uname,age)
    json_data = json.dumps({'code':200,'msg':s})
    return json_data,{'Content-Type':'application/json'}#设置响应头为JSON的格式
    #需要自定义错误页面时，可以返回相对的状态码 如404 500
    # return jsonify({'code':200,'msg':s})

@app.route('/post',methods=['get','post'])
def post_view():
    if request.method=='GET':
        return render_template('jq-post.html')
    elif request.method=='POST':
        #根据用户年龄显示不同的结果
        data = {'code':1200,'msg':'post is ok.'}
        if int(request.form.get('age',0))>100:
            data ={'code':1201,'msg':'age is so big'}
        return data #flask1.1.1支持字典格式

@app.route('/ajax',methods=['get','post'])
def ajax_view():
    return render_template('jq-ajax.html')
@app.route('/ajax_server',methods=['get','post'])
def ajax_server():
    if request.method =='GET':
        import time
        time.sleep(2)
        data = {'code':1200,'msg':'ok'}
        return data
    elif request.method=='POST':
        # uname=request.form.get('uname')#b表单格式提交的数据
        uname = request.json.get('uname')
        data = {"code":1200,'msg':'welcome %s'%uname}
        return data

@app.route('/cross')
def cross_view():
    return render_template('cross.html')

if __name__ =="__main__":
    app.run(debug=True)