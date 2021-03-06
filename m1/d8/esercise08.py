dict_goods_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []

def input_purchase_info():
    """
    获取用户购买信息
    :return:
    """
    goods_id = int(input("请输入要购买的商品的编号："))

def purchase():
    print_goods_info()


def settlement():
    pass


def print_goods_info():
    """
    输出商品信息
    :return:
    """
    for key, value in dict_goods_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

def input_info(number):
    """
    获取用户执行指令
    :param number: 执行指令
    :return:
    """
    purchase() if number == 1 else settlement()


def purchase_():

    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            for key, value in shang_pin_info.items():
                print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
            while True:
                cid = int(input("请输入商品编号："))
                if cid in shang_pin_info:
                    break
                else:
                    print("该商品不存在")
            count = int(input("请输入购买数量："))
            list_order.append({"cid": cid, "count": count})
            print("添加到购物车。")
        elif item == "2":
            zong_jia = 0
            for item in list_order:
                shang_pin = shang_pin_info[item["cid"]]
                print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
                zong_jia += shang_pin["price"] * item["count"]
            while True:
                qian = float(input("总价%d元，请输入金额：" % zong_jia))
                if qian >= zong_jia:
                    print("购买成功，找回：%d元。" % (qian - zong_jia))
                    list_order.clear()
                    break
                else:
                    print("金额不足.")


gou_wu()