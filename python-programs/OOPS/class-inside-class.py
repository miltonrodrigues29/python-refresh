from this import d


class Student:
    def __init__(self,name,rollno):
         self.name = name
         self.rollno = rollno
         self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    

    class Laptop:
        
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8"
        
        def show(self):
            print(self.brand, self.cpu, self.ram)
    


s1 = Student("Milton",16)
s2 = Student("Naveen",22)

s1.show()
print("------------------------")
s2.show()


