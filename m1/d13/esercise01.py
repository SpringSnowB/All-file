"""
定义父类
动物：吃
定义子类
狗：
鸟：
"""
class Animal:
    def eat(self):
        print("吃")

class Dog(Animal):
    def run(self):
        print("跑")
class Bird(Animal):
    def fly(self):
        print("飞")

aniaml = Animal()
dog = Dog()
bird = Bird()

print(isinstance(aniaml,Animal))
print(isinstance(bird,Animal))
print(isinstance(aniaml,Bird))
print(isinstance(dog,Dog))

print(issubclass(Animal,Dog)) #父类和子类不是一种类型
print(issubclass(Dog,Animal)) #子类和父类是一种类型
print(issubclass(Dog,Bird)) #子类和子类不是一种类型

print(type(dog) == Dog)    #True
print(type(dog) == Animal) #False
print(type(dog) == Bird)   #False
