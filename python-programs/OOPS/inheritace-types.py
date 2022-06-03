class A:
    def __init__(self,a_name):
        self.a_name = a_name
        print("Init method of class A")
    

class B(A):
    def __init__(self, b_name,a_name):
        self.b_name = b_name
        A.__init__(self,a_name)


class C(B):
    def __init__(self,c_name,b_name,a_name):
        self.c_name = c_name
        B.__init__(self, b_name,a_name)

    def display_names(self):
        print("A name : ",self.a_name)
        print("B name : ",self.b_name)
        print("C name : ",self.c_name )

obj1 = C("milton","christon","veniston")
obj1.display_names()
        
    
        
 

