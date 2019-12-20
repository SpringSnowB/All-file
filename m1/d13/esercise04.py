class V:
    def __init__(self, x=0):
        self.x = x
    def __str__(self):
        return "%s"%self.x
    def __sub__(self, other):
        return V(self.x - other.x)

    def __isub__(self, other):
        self.x -= other.x
        return self
v1 = V(16)
v2 = V(11)
re = v1-v2
print(re)
print(v1.__sub__(v2))
v1 -= v2
print(v1)