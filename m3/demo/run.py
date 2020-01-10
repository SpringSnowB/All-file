from flask import Flask,render_template,jsonify
import json
app = Flask(__name__)

@app.route('/get_data')
def get_data_view():
    return render_template('get_data.html')

@app.route('/get_data_server')
def get_data_server():
    cartdata = {
        "username": "qi941129",
        "password": "123",
        "cart": [
            {
                "id": "1",
                "count": "11",
                "name": "蓝色小尺寸",
                "default_image_url": "http://114.116.244.115:7001/media/2_5pdezhv.jpg",
                "price": 100,
                "selected": "true",
                "sku_sale_attr_name": ["安踏A/尺寸：", "安踏A/颜色："],
                "sku_sale_attr_val": ["15寸", "蓝色"]
            },
            {
                "id": "2",
                "count": "9",
                "name": "红色大尺寸",
                "default_image_url": "http://114.116.244.115:7001/media/3_JGA6F97.jpg",
                "price": 10000,
                "selected": "true",
                "sku_sale_attr_name": ["安踏A/尺寸：", "安踏A/颜色："],
                "sku_sale_attr_val": ["18寸", "绿色"]
            },
            {
                "id": "3",
                "count": "10",
                "name": "蓝色小尺寸",
                "default_image_url": "http://114.116.244.115:7001/media/4_z3FdRMq.jpg",
                "price": 1000,
                "selected": "true",
                "sku_sale_attr_name": ["安踏B/尺寸：", "安踏B/颜色："],
                "sku_sale_attr_val": ["18寸", "蓝色"]
            }
        ]
    }
    # return json.dumps(cartdata),{'Content-Type':'application/json'}
    return jsonify(cartdata)


@app.route('/get_data_list')
def get_data_list_view():
    return render_template('get_data_list.html')

@app.route('/get_data_list_server')
def get_data_list_server():
    skulist = [
        {
            "model": "goods.sku",
            "pk": 1,
            "fields": {
                "create_time": "2019-12-04T21:25:10.613",
                "update_time": "2019-12-23T20:04:15.419",
                "name": "\u5b89\u8e0fA\u84dd\u8272\u5c0f\u5c3a\u5bf8",
                "caption": "\u84dd\u8272\u5c0f\u5c3a\u5bf8",
                "SPU_ID": 1,
                "price": "100.00",
                "cost_price": "1000.00",
                "market_price": "1000.00",
                "stock": 911, "sales": 1089,
                "comments": 100,
                "is_launched": 'true',
                "default_image_url": "2_5pdezhv.jpg",
                "version": 12
            }
        },
        {
            "model": "goods.sku",
            "pk": 2,
            "fields": {
                "create_time": "2019-12-04T21:25:58.561",
                "update_time": "2019-12-13T17:02:11.021",
                "name": "\u5b89\u8e0fA\u7ea2\u8272\u5927\u5c3a\u5bf8",
                "caption": "\u7ea2\u8272\u5927\u5c3a\u5bf8",
                "SPU_ID": 1,
                "price": "10000.00",
                "cost_price": "1000.00",
                "market_price": "1000.00",
                "stock": 929, "sales": 1071,
                "comments": 1000,
                "is_launched": 'true',
                "default_image_url": "3_JGA6F97.jpg",
                "version": 7
            }
        },
        {
            "model": "goods.sku",
            "pk": 3,
            "fields": {
                "create_time": "2019-12-04T21:26:23.278",
                "update_time": "2019-12-13T17:02:22.045",
                "name": "\u5b89\u8e0fB\u7ea2\u8272\u5927\u5c3a\u5bf8",
                "caption": "\u84dd\u8272\u5c0f\u5c3a\u5bf8",
                "SPU_ID": 2,
                "price": "1000.00",
                "cost_price": "1000.00",
                "market_price": "1000.00",
                "stock": 931,
                "sales": 1069,
                "comments": 1000,
                "is_launched": 'true',
                "default_image_url": "4_z3FdRMq.jpg",
                "version": 4
            }
        }
    ]
    return jsonify(skulist)

if __name__=="__main__":

    app.run(debug=True)