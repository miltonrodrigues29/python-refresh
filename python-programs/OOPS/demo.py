from ctypes import sizeof

import sys


class Computer:


    def __init__(self):
        self.name = "Milton"
        self.age  = 22
        self.gender = "Male"
        
    def config(self):
        print("Config is ",self.name, self.age)
    
    def compare(self, other):
        if self.age == other.age:
            print("Objects age match!")
        else:
            print("Obhects age does not match")

com1 = Computer()
com2 = Computer()
com1.config()
com2.name = "Flavia"
com2.age = 22 
com2.config()
print(id(com1))
print(id(com2))   #heap memory address
print(sys.getsizeof(com1))
print(sys.getsizeof(com2))
print("------------------------------")
com1.compare(com2)

