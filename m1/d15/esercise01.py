"""
创建模块esercise02使用三种方式调用当前模块的成员  fun01  fun02 fun03
"""

import esercise02 as er
myclass = er.MyClass()
er.fun01()
myclass.fun02()
myclass.fun03()

from esercise02 import fun01
fun01()

from esercise02 import *
fun01()
MyClass.fun03()