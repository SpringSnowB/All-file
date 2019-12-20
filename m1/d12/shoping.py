"""
用MVC思想构建购物管理
"""

class ShoppingModel:
    def __init__(self):
        self.__dict_goods_info = {
            101: {"name": "屠龙刀", "price": 10000},
            102: {"name": "倚天剑", "price": 10000},
            103: {"name": "九阴白骨爪", "price": 8000},
            104: {"name": "九阳神功", "price": 9000},
            105: {"name": "降龙十八掌", "price": 8000},
            106: {"name": "乾坤大挪移", "price": 10000}
        }
    @property
    def dict_goods_info(self):
        return self.__dict_goods_info

class ShoppingManagerControll:
    def __init__(self):
        self.__dict_order = {}

    def create_order(self,good_id,count):
        self.__dict_order[good_id] = count

    def calculate_total_price(self):
        """
        计算总价
        :return:总价
        """
        total_price = 0
        for key,value in self.__dict_order.items():
            commodity = ShoppingModel().dict_goods_info[key]
            total_price += commodity["price"] * value
        return total_price

    def clear_order(self):
        """
        清空购物车
        """
        self.__dict_order = {}


class ShoppingManagerView():

    def __init__(self):
        self.__controll = ShoppingManagerControll()

    def main(self):
        self.__display_goods_info()
        self.__select_service()

    def __select_service(self):
        user_input = int(input("1键购买，2键结算。"))
        if user_input == 1:
            self.__create_order()
        elif user_input ==2:
            self.__settlement()
        else:
            print("输入错误！")

    def __create_order(self):
        while True:
            good_id = input("请输入要购买商品的编号：")
            if good_id == "":
                break
            good_id = int(good_id)
            if good_id not in ShoppingModel().dict_goods_info.keys():
                print("商品不存在，请重新输入。")
            else:
                count = int(input("请输入购买数量："))
            self.__controll.create_order(good_id,count)
        self.__select_service()


    def __display_goods_info(self):
        for key,value in ShoppingModel().dict_goods_info.items():
            print("编号：%d,名称：%s,单价：%d."%(key,value["name"],value["price"]))

    def __settlement(self):
        total_price = self.__controll.calculate_total_price()
        self.__paying(total_price)

    def __paying(self,total_price):
        while True:
            money = float(input("总价%d元，请输入金额：" % total_price))
            if money >= total_price:
                print("购买成功，找回：%d元。" % (money - total_price))
                self.__controll.clear_order()
                break
            else:
                print("金额不足。")

view = ShoppingManagerView()
view.main()