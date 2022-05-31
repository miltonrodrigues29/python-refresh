class Car:
    wheels = 4         #class namespace #change will effect the all objects
  
    def __init__(self):
        self.mil = 10                    #instace name space
        self.com = "BMW"
    
    
    


c1 = Car()
c2 = Car()


c1.mil = 8
c2.com = "Ferrari"

Car.wheels = 10

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)



