# 0,1,1,2,3
# f1=0
# f2=1
# temp = f2 + f1
class Fibonacci:
    def fib(n):
        f1=0
        f2=1
        if n<=0:
            print("Pease enter value greater than 0")
        elif n==1:
            print("Fibonacci Sequence of numbers upto :",n,": ",f1)
        else:
            print("Fibonacci Sequence of numbers upto :", n,": ") 
            count  =0 
            while count<n:
                print(f1)
                temp = f1+f2
                f1=f2
                f2=temp
                count+=1


n = int(input("Enter the value of n :"))
o = Fibonacci
o.fib(n)




                