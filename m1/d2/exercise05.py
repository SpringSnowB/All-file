"""
变量交换
"""
# 通用变量交换
data01="sun"
data02="zhu"
temp=data01
data01=data02
data02=temp
# python中变量交换
data02,data01=data01,data02

print(data01)
print(data02)
