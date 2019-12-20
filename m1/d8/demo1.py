"""
默认参数
   原则：你给我我用你的，你不给我我用我的
   默认参数必须从右往左依次存在
"""

def fun01(p1 = "",p2 = 8,p3 = .0):
    print(p1)
    print(p2)
    print(p3)

fun01()
fun01("mm",10,9.8)

# 关键字实参 + 默认参数：实际参数可以随意传递
fun01(p2= 1000000)

#位置形参：实参必须传递
def fun01(p1 = "",p2 = 8,p3 = .0):
    print(p1)
    print(p2)
    print(p3)


def fun02(*p1):
    print(p1)

# fun02()
# fun02(4,5,6765,4)
# fun02(a=1,b=2,c=3)#报错

#命名关键字形参：星号元组形参后面的参数
#   要求实参必须是关键字实参
def fun04(*args,a = 9,b = 0):
    print(args)
    print(a)
    print(b)
fun04(321,43,225,65,8,a = 1,b = 9)

# a必填 *选填  b、c必须以命名关键字的方式填写，
# 有默认值，可以选填，但使用默认值
def fun05(a,*,b=4,c=""):
    print(a)
    print(b)
    print(c)

fun05(5,c="ooo")


#双星号字典形参
def fun06(**kwargs):
    print(kwargs)

fun06(a = 1,b=2,c=3) #输出字典