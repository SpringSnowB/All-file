from flask import Flask,request
import json

app = Flask(__name__)
@app.route('/get')
def get_server():
    fun = request.args.get('callback')
    data = 'from 5001'
    print(fun+'("'+data+'")')
    return fun+'("'+data+'")'

@app.route('/get_json')
def get_json():
    fun = request.args.get('callback')
    data = {"code":1200,"msg":'ok'}
    return fun+'('+json.dumps(data)+')'

if __name__=="__main__":
    app.run(debug=True,port=5001)