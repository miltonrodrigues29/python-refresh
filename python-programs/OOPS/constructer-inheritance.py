class A:
    def __init__(self):
        print("Init method of A")

    def feature1(self):
        print("Feature 1 in a working..")

    def feature2(self):
        print("Feature 2 working..")


class B():


    def __init__(self):
        print("Init method of B")

    
    def feature1(self):
        print("Feature 1 in b working..")

    def feature4(self):
        print("Feature 4 working..")


class C(A,B):
    def feat(self):
        super().feature4()
    

c = C()
c.feat()


