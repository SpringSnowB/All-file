"""
列表推导式嵌套
"""
list_poker = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
list_color = ["红桃","黑桃","方片","梅花"]
list_poker_color = [color + poker for poker in list_poker for color in list_color]
print(list_poker_color)


# list_all = []
# for i in range(1,7):
#     for j in range(1,7):
#         for k in range(1,7):
#             list_all.append((i,j,k))
# print(list_all)

list_all = [(i,j,k) for i in range(1,7) for j in range(1,7) for k in range(1,7)]
print(list_all)