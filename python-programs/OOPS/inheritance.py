class A:
    def feature1(self):
        print("Feature 1 is working..")


    def feature2(self):
        print("Feature 2 is working..")



class B:
    def feature3(self):
        print("Feature 3 is working..")
    
    def feature4(self):
        print("Feature 4 is working..")



class C(A,B):
    def feature5(self):
        print("Feature 5  working..")



#Multiple inheritace is possible in python
o = B()
o.feature3()
o.feature4()
o.feature1()

a = A()
a.feature3()

c = C()



    
    