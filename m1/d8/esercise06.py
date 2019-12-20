"""

"""
def fun01(*args,**kwargs):
    print(args)
    print(kwargs)

def fun02(a,b,*args,c=0,d=0,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

fun01(1,2,3,4,{"s":1,"c":19})
fun01()
fun01({"s":1,"c":19})
fun01(s=2,k=9)

fun01(1,2,3,4)

fun02(12,14,14,15,c=9,d=2,s=1,k=0,j=10)
