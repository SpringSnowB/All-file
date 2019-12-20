"""
07
"""
class Wife:
    def __init__(self, name="",height=160,weight=50,age=22):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def __str__(self):
        return "%s,%d,%d,%d"%(self.name, self.height, self.weight, self.age)
list_wife = [
    Wife("KK",156,53,38),
    Wife("KK",156,53,38),
    Wife("KK",156,53,38),
    Wife("KK",156,53,38),
    Wife("DD",166,40,22),
    Wife("SS",178,51,27),
    Wife("aa",164,68,25),
]
def fun(list_wife):
    for item in list_wife:
        if item.name =="KK":
            yield item
result = tuple(fun(list_wife))
print(result)