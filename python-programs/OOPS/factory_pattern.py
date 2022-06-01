from abc import ABC, abstractmethod
from distutils.log import error
from secrets import choice

class IPerson(ABC):
    
    @abstractmethod
    def print_method(self):
        """HELLO"""

class Person(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"
    def print_method(self):
        print("Iam Person")


class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher name"

    def print_method(self):
        print("Iam Teacher")



class PersonFactory:
    def build_person(person_type):
        if person_type=="Person":
            return Person()
        elif person_type =="Teacher":
            return Teacher()
        else:
            return Exception
        
        

if __name__ == "__main__":
    choice = input("Choice: ")
    p = PersonFactory.build_person(choice)
    p.print_method()
    


