"""

在终端中录入商品信息（名称/价格）
如果名称是空，则停止
   将所有商品名称与价格打印出来（一行一个）
   如果录入了“游戏机”，则单独打印其价格
   要求：商品不能重复录入
"""
dict_goods = {}
while True:
    key = input("请输入商品名：")
    if key =="":
        break
    if key not in dict_goods.keys():
        value = int(input("请输入商品的价格："))
        dict_goods[key] = value
    else:
        print("商品重复，请重新录入")

    if key =="游戏机":
        for v in dict_goods.values():
            print(v)
for k ,v in dict_goods.items():
    print("%s:%d"%(k,v))

