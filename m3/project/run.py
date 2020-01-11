from flask import Flask,render_template,request,jsonify
import json,time


app = Flask(__name__)

@app.route('/')
def index_view():
    return render_template('hello.html')

@app.route('/data',methods=['get','post'])
def get_data():
    size = request.args.get('size')
    file = open('/home/tarena/code/m3/project/comment.data')
    all_data = json.loads(file.read())
    file.close()
    if not size:
        data = all_data[:10]
    else:
        size = int(size)
        data = all_data[size:size+10]
        if not data:
            return jsonify({"code":201,"error":"没有数据了"})
    return jsonify({"code":200,"data":data})

@app.route('/add',methods=['get','post'])
def add_data():
    name = request.form.get('name')
    content = request.form.get('content')
    try:
        file = open('/home/tarena/code/m3/project/comment.data')
        all_data = json.loads(file.read())
        file.close()
        data = {
            'num':len(all_data)+1,'username':name,
            'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
            'content':content
        }
        all_data.append(data)
        file = open('/home/tarena/code/m3/project/comment.data','w')
        file.write(json.dumps(all_data))
        file.close()
    except Exception as e:
        print(e)
        return jsonify({'code':201,'error':'内容发送失败'})
    return jsonify({'code':200,'data':'内容发布成功'})




if __name__=="__main__":
    app.run(debug=True)