class Student:
    school = "Milton"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1, self.m2, self.m3)/3
    
    def get_m1(self):   #below function that deal with instance variables
        return self.m1   #accessor methods
    
    def set_m1(self,value):   #mutator methods
        self.m1 =value
    
    def set_m2(self, value):
        self.m3 = value
    
    def print_marks(self):
        print(self.m1, self.m2, self.m3)

    @classmethod
    def getSchool(cls):     #function deals with class variables
        print(cls.school)

    @staticmethod
    def info():
        print("This is Student Class, in abc module")



o1 = Student(99,98,97)
o1.print_marks()
o1.set_m1(69)
print(Student.getSchool())
Student.info()

