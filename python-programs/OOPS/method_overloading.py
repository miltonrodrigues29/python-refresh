#not possible in java
#but can be done using some tricks like passing default values to the arguement

class Addition:

    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a                    



o1 = Addition()
print(o1.add(1))
print(o1.add(1,2))