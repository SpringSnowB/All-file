import json
cartdata={
    "username":"qi941129",
    "password":"123",
    "cart":[
        {
            "id":"1",
            "count":"11",
            "name":"蓝色小尺寸",
            "default_image_url":"http://114.116.244.115:7001/media/2_5pdezhv.jpg",
            "price":100,
            "selected":True,
            "sku_sale_attr_name":["安踏A/尺寸：","安踏A/颜色："],
            "sku_sale_attr_val":["15寸","蓝色"]
        },
        {
            "id":"2",
            "count":"9",
            "name":"红色大尺寸",
            "default_image_url":"http://114.116.244.115:7001/media/3_JGA6F97.jpg",
            "price":10000,
            "selected":True,
            "sku_sale_attr_name":["安踏A/尺寸：","安踏A/颜色："],
            "sku_sale_attr_val":["18寸","绿色"]
        },
        {
            "id":"3",
            "count":"10",
            "name":"蓝色小尺寸",
            "default_image_url":"http://114.116.244.115:7001/media/4_z3FdRMq.jpg",
            "price":1000,
            "selected":True,
            "sku_sale_attr_name":["安踏B/尺寸：","安踏B/颜色："],
            "sku_sale_attr_val":["18寸","蓝色"]
        }
    ]
}


print(type(cartdata["cart"]))
for k,v in cartdata.items():
    if type(v)==type(cartdata["cart"]):
        for i in range(len(v)):
            print(v[i])
    else:
        print(v)