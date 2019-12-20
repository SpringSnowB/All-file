"""
显示几斤零几两
"""

wight = int(input("请输入两："))
jin = wight // 10
liang = wight % 10
print("%d斤零%d两"%(jin,liang))