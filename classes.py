class MyClass:
    x=5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
        self.gender="male"
    
    def myfunc(self):
        print("Hello my name is: "+self.name)

p1 = Person("John",36)


p1=Person("John",36)
print(p1.name)
print(p1.age)
print(p1.gender)
p1.myfunc()

