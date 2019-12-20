"""
定义数据结构，存储一下信息：
 --多个人的多个爱好
 打印qtx的所有爱好，一行一个
 所有人的所有爱好，一行一个

"""
dict_like = {
    "qtx": ["编码","看书","跑步"],
    "lzmly": ["看电影","编码","美食","唱歌"]
}
print("qtx的爱好有：")
for item in dict_like["qtx"]:
    print(item)
for key in dict_like.keys():
    print("%s的爱好有："%(key))
    for value in dict_like[key]:
        print(value)
