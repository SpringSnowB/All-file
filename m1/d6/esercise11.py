"""
定义数据结构存储一下信息：
————多个城市的多个景区和美食
打印北京所有美食，一行一个
打印所有城市，一行一个
打印所有城市的所有景区，一行一个
"""
dict_city = {
    "北京": {
        "景区":["天安门","天坛","故宫"],
        "美食":["驴打滚","豆汁"]
    },
    "四川": {
        "景区": ["九寨沟","宽窄巷子"],
        "美食": ["火锅","串串香"]
    }
}

print("北京的美食有：")
for food in dict_city["北京"]["美食"]:
    print(food)

print("所有城市有：")
for city in dict_city.keys():
    print(city)

for city in dict_city.keys():
    print("城市%s的景区有："%(city))
    for site in dict_city[city]["景区"]:
        print(site)