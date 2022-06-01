class A:
    def add(self):
        print("Adding two numbers")
    


class B(A):
     def add(self):
         print("Adding in class B")


b = B()
b.add() #this will call the add function present in class B
