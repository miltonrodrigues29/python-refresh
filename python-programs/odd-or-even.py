class Number:
    def __init__(self,n):
        self.number = n
    
    def check(self):
        if self.number % 2 == 0:
            print("{0} is even".format(self.number))
        else :
            print("{0} is odd".format(self.number))



n = int(input("Enter the Number"))
c = Number(n)
c.check()
    
        


