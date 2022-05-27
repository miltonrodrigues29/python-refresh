
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname,self.lastname)



# x= Person("John","Doe")
# x.printname()
class Kid(Person):
    def __init__(self,fname,lname):
        Person.__init__(self, fname,lname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

        
        
x = Student("Mike","Olsen")
x.printname()
