"""
斤两转换
"""
def jin_to_liang(weight):
    return weight // 16,weight % 16   #元组

weight = int(input("请输入重量："))
jin_weight,liang_weight = jin_to_liang(weight)
print("%d斤，%d量"%(jin_weight,liang_weight))