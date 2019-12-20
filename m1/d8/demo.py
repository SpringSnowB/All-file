"""
函数参数
   实际参数
"""
def fun01(p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)

fun01(1,2,3)

list01 = [5,6,7]
touple01 = (15,16,17)
set01 = {"a","b","c"}
dict01 = {"a":1,"b":2,"c":3}
fun01(*list01)
fun01(*touple01)
fun01(*set01)  #无意义
fun01(*dict01)  #无意义


#关键字实参：根据参数名称与形参进行对应
fun01(p2=4,p1=5,p3=9)

dict02 = {"p1":1,"p3":2,"p2":3}
fun01(**dict02)
