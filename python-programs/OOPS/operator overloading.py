# a =10
# b =11
# # print(a+b)
# # print(int.__add__(a,b))  #int class has a method called __add__
## if you want to add two student, you need to overload the + operator. because your string knows + operator, int knows + operator, but your Student class does not know what is + operator

from enum import Flag
from operator import truediv


class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        m1 = self.m1+ other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self,other):
        t1 = self.m1 + self.m2
        t2 = other.m1 + other.m2
        if t1>t2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

        


    


o1 = Student(10,20)
o2 = Student(30,40)

s3 = o1+o2
print(s3.m1)
print(s3.m2)


print(o1)
print(o2)





